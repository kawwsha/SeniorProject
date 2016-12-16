function [ LogoPresent ] = CODandSiftBoolean(imageFile,logoFile )
%Combines sift and cascade object detector
%   runs all of the possible boxes through sift to narrow them down

%connect to db
conn = database('sentimentdb','username','password','Vendor','PostgreSQL',...
                'Server','localhost')
            
% query db for image ids and urls
sqlquery = 'SELECT id, media_images, contains_logo from image';
curs = exec(conn,sqlquery);

setdbprefs('DataReturnFormat','cellarray');

%curs = fetch(curs);
%curs.Data;

rowlimit = 1

while ~strcmp(curs.Data, 'No Data')
        curs = fetch(curs,rowlimit);
        imgId = curs.Data(:,1)
        imgIdDb= imgId{1}
        imgUrl = curs.Data(:,2) 
        imgLogo = curs.Data(:,3)

%sets LogoPresent to false, assumes no logo
LogoPresent=0;

%loads trained object detector
detector = vision.CascadeObjectDetector('StarbucksDetector.xml');

%sets image and logo
logo=imread('sbux.png');
img = imread(imgUrl{1});

%Finds boxes for object detector matches
bbox = step(detector,img);

%runs SIFT if there are some possible matches
if ~isempty(bbox)
    
    for i=1:size(bbox,1)
        %gets subimage
        subImage=imcrop(img,bbox(i,:));
        imshow(subImage);hold on;
        %runs subimage in SIFT
        if SIFT2(subImage,logo)
            LogoPresent=1;
        end
            
    end
end 
%export to db
colnames = {'contains_logo'};
data = LogoPresent;
%whereclause = 'where id = imgIdDb';
exdata(1,2) = {LogoPresent};
insert(conn, 'image', colnames , data);
end
end

