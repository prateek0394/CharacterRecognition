for i = 1:1%6284:12503

    img = imread(strcat('trainPaper/',int2str(1),'.Bmp'));
    
    % Extract HOG features and HOG visualization
    [hog_2x2, vis2x2] = extractHOGFeatures(img,'CellSize',[4 4]);
    [hog_4x4, vis4x4] = extractHOGFeatures(img,'CellSize',[8 8]);
    [hog_8x8, vis8x8] = extractHOGFeatures(img,'CellSize',[12 12]);

    % Show the original image
    figure;
    subplot(2,3,1:3); imshow(img);

    % Visualize the HOG features
    subplot(2,3,4);
    plot(vis2x2);
    title({'CellSize = [4 4]'; ['Feature length = ' num2str(length(hog_2x2))]});
 
    subplot(2,3,5);
    plot(vis4x4);
    title({'CellSize = [8 8]'; ['Feature length = ' num2str(length(hog_4x4))]});

    subplot(2,3,6);
    plot(vis8x8);
    title({'CellSize = [12 12]'; ['Feature length = ' num2str(length(hog_8x8))]});

    featureVector
end