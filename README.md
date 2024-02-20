### snps-to-2dcnn-converter ###

**Description**

- The primary goal of this project is to convert sequential data into 2D images with 3 channels and use the images to train a CNN model.
    * The sequential data is the single nucleotide polymorphisms (SNPs) of the strains.
    * The 2d images are the SNPs of the strains in a 3d matrix format[w,h,c].
    * The CNN model is used to predict the drug resistance of the strains. And the model was built from scratch.

**Dataset**

- Under the Final dataset. We have the follwing features
    * prename: This is the isolate name.
    * CIP: This is the isolate's response to the drug ciprofloxacin.
    * CTX: This is the isolate's response to the drug cefotaxime.
    * CTZ: This is the isolate's response to the drug ceftazidime
    * GEN: This is the isolate's response to the drug gentamicin.
    * Image: This is the isolate's genetic makeup, represented as an 2D image.
        
        `` The data are encoded as follows: 0 = Susceptible, 1 = Resistant ``  
 

***Install the required packages***
    
     pip install -r requirements.txt
