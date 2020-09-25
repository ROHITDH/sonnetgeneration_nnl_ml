Introduction: 
-------------	
				Here we are going to create the "character-level" model for the generation of rhyme scheme sonnet. This model
				will going to generate the 14 line poem (sonnet) as the
				output.


Contents:
----------	
			1] Installation setup -- packages
			2] Downloading of required resource
			3] Model creation
			4] Generation of sonnet from model
			5] Theory/Techniques Used
			6] Technologies/Platform:
			7] Grade Test

			(both in directly python / jupyter nootbook)


--------------------------------------------------------------------------
Procedure: 
----------

1] Package installation:
 		Open the command prompt/any alternatives and install the following packages.

 		Example: pip install tensorflow

 		These are the required packages:

 		https://drive.google.com/file/d/1RjaUGtvLzud2T3WA5Z-Kgczb_DCsnD2G/view?usp=sharing

 				1. Download "requirements.txt" from the above link
 				2. go to the directory where you downloaded this file
 				3. then run this command
 					pip install -r requirements.txt
 				4. This will directly install all the required packages.

2] Downloading the resource:
		download all these codes on github directly by downloading zip file
		and extract it
								or

		run this command to git from github
			git clone  https://github.com/ADA-Canara-Engineering/sonnet

3] Model Creation:
		1] after unzipping/downloading the resource, go to
			"MODEL CREATION" directry 

			[cd MODEL CREATION]

		2] If you want to run the entire program and to create the model,
			run : python creation.py

			Note:
			This will going to take more time, since the training the model is pre-set to 60 compiling dataset.(Epochs)

			
			Another way to run the program and create model is to use
			Jupytor nootbook, For this install "jupyter nootbook" from here: --LINK--
				in jupyter nootbook, open "creation_jupyter_note_book.ipynb" file, and run each block or run all block at a time.

			After the completion of training, the model "sonnet_gen_model.h5" will going to create in same directory

4] Generation of sonnet from model
		1] copy the generated model to the OUTPUT folder/dir,
			(here it's already model is generated and placed in 
			"OUTPUT" folder)
		2] go to directory called "OUTPUT" and run this command to
			generate the sonnet from the model that we created in step-3.
			
			python main.py


			If you are using jupyter nootbook, than open "main_jupyter_nootbook.ipynb" 
			and run this to generate the sonnet.
		3] Even we can create sonnet from google colab
			https://colab.research.google.com/drive/11KAKfFbAmxbb1Ge6P9N02otFqp4GywgV?usp=sharing


------------------------------------------------------------------------
5] Theory/Techniques Used:

	a. model creation
		1] Loading the provided dataset and analysing the  character 
			length of sonnet and average character per line
		2] View of the dataset in details by plotting graph of length of 
			characters in each sonnet 
		3] Here the average length of a sonnet is found to be 625 
			characters for a sonnet
		4] Vectorization for the generation of next characters based on 
			the sequence of first line, intially 40 characters are loading from dataset with previous sample of 3.
		5] Storing all the predicted unique characters and mapping it 
			with indices
		6] Vectorizing the generated sequence with numpy array
		7] By using sequential regression in keras, and using recurrent 
			neural network for sequence prediction, creation of model.
		8] Next we have to train this probability value generating model
			with the data.(Epoch) Here 625 characters for 4 different 
			probability distribution values "0.2, 0.5, 1.0, 1.3" and 60 
			triels were done. If the distribution of characters is inversely
			proportional to randomness.
		9] character prediction loss will going to be 3.11 to 1.79 from 
			initial training to end of training, Average loss is found 
			to be 2.45% character loss.
		10] than finally saving the trained model.

	b. Generating Sonnet
		1] from the data, it will going to take rendomly some text 
			sequence, and based on the prediction created by the model,
			the nexr characters are generated.
		2] concerting the initial grabbed character sequence to 
			vectorizing and adding the pre-generated sequence along with 
			the character predicted by the model to the new string.

-------------------------------------------------------------------------
6] Technologies/Platform:
	GCD
	Python
	TensorFlow
	Django, js, bootstrap, js, jquery

------------------------------------------------------------------------

7] Grade test:
	Readability test --  Flesch Kincaid Grade Level
	here are the 10 randomanly generated sonnet from the created model, 
	Flesch Kincaid Grade Level test is done on these generated sonnets and 
	the result of 43.28 is obtained which best suits the property of sonnet.

	30-50	score ensures  :
	difficult to read, best understood by college graduates
	so this ensures sonnet readebality.
	(source: https://yoast.com/flesch-reading-ease-score/ )

-------------------------------------------------------------------------

