function [ im ] = SIFT2(Image,Logo)
%PUZZLE finds matching points between the image and the pieces
%   using sift

%read in images
im=Image;
Logo=Logo;

%convert images to greyscale
im1=single(rgb2gray(im));
piece1g=single(rgb2gray(Logo));

%find points in puzzle and display
[f1,da]= vl_sift(im1,'PeakThresh',1);
%sets figure and displays points for puzzle
% figure;
% imshow(im);
% hold on;
% h1=vl_plotframe(f1);

%find points in piece1 and display
[f2,db]= vl_sift(piece1g,'PeakThresh',1);
%sets a figure
%figure;
%shows piece1 in figure
%imshow(Logo);
%holds and then plots points from above onto piece1
%hold on;
%h1=vl_plotframe(f2);

%find matches between puzzle and piece1
[matches, scores] = vl_ubcmatch(da,db,3);

%gets number of matches
numMatches = size(matches,2);
%finds size of puzzle and piece 
dh1 = max(size(Logo,1) - size(im,1),0);
dh2 = max(size(im,1) - size(Logo,1),0);
%sets the figure
%figure; clf;
%imagesc([padarray(im,dh1,'post') padarray(Logo,dh2,'post')]);
%o=size(im1,2);
%line([f1(1,matches(1,:)); f2(1,matches(2,:)) + o], [f1(2,matches(1,:)); f2(2,matches(2,:))]);
%labels number of matches
%title(sprintf('%d tentative matches', numMatches));
%axis image off;

%get x and y coordinates of puzzle and piece1
x1=f1(1, matches(1, :));%puzzle
x2=f2(1, matches(2,:));%piece1
y1=f1(2, matches(1, :));%puzzle
y2=f2(2, matches(2,:));%piece1
end

