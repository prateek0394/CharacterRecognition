for i = 13:13
    img = imread(strcat('train/',int2str(i),'.Bmp'));
    
    %STEP 1 Resizing to 50x50
    img = imresize(img,[50 50]);
    imwrite(img, strcat('IP_Pipeline/',int2str(i),'_1.Bmp'), 'bmp')
    
    %STEP 2 Converting to Grayscale
    [a,b,c] = size(img);
     if c==3
         img = rgb2gray(img);
     end
    imwrite(img, strcat('IP_Pipeline/',int2str(i),'_2.Bmp'), 'bmp')
    
    %STEP 3 
    img = medfilt2(img);
    imwrite(img, strcat('IP_Pipeline/',int2str(i),'_3.Bmp'), 'bmp')
    
    %STEP 4 Otsu Thresholding and Converting to binary
    level = graythresh(img);
    img = im2bw(img,level);
    imwrite(img, strcat('IP_Pipeline/',int2str(i),'_4.Bmp'), 'bmp')
    
    [hog_8x8, vis8x8] = extractHOGFeatures(img,'CellSize',[8 8]);
end