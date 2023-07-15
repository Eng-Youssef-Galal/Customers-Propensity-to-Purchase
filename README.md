# Customer-s-Propensity-to-Purchase
ML Web Applications for Customer’s Propensity to Purchase

# The Business Problem
While a website can have many visitors, only a small proportion may actually buy from the business. Currently, the business may be spending money to retarget these visitors using maybe advertisements on Social media platforms like Facebook. It is only logical for it to optimize this activity by targeting only the most valuable prospects who are more likely to make a purchase. Our task is exactly this – to build a Machine Learning model that predicts the propensity of purchase for a particular customer using historical data.

# Build and Save a Machine Learning Model
We will start by having a look at our training data. For the sake of simplicity, I have chosen a subset of features from the dataset. I have saved this subset for loading it later in our Streamlit Application.

Let us have a closer look at the columns in the dataset:

‘UserID’ – Unique Identifier for each customer

‘basket_add_detail’ – A binary variable indicating if the customer added an item to the basket from the product detail page

‘promo_banner_click’ – A binary variable indicating if the customer clicked on any promotional banners

‘sign_in’ – Another binary variable, indicating if the customer signed into our website.

‘returning_user’ – Again, a binary variable indicating if the customer is a returning visitor to our website.

‘saw_homepage’ – A binary variable indicating if the customer saw the homepage of the website

‘ordered’ – Our target variable. A binary variable indicating if the customer placed an order.

# Web Application using Streamlit
Building a Multipage Application is usually one of the most common requests that you would get from your project stakeholders. Here, we will see how to build a two-page application in Streamlit using radio buttons. To do this we will need to write 3 python (.py) scripts. Two of them will be the tasks that need to be performed on respective pages and one script to integrate these two scripts. In our case, page 1 will show details about the training data, and the code for this is written in “training.py”. Page 2 will have user input fields and predictions. The code for this is written in “predict.py”. These two files will be integrated using a third python script called “Streamlit_main_app.py”.

# Final result

![1](https://github.com/Eng-Youssef-Galal/Customer-s-Propensity-to-Purchase/assets/138930263/153f310f-aea7-42e3-b60d-cd6626c50194)


![2](https://github.com/Eng-Youssef-Galal/Customer-s-Propensity-to-Purchase/assets/138930263/328a1900-5373-4c5e-b9f9-4671c2484661)


![3](https://github.com/Eng-Youssef-Galal/Customer-s-Propensity-to-Purchase/assets/138930263/ea296b23-574b-44fa-b949-b36c4a2a7675)

