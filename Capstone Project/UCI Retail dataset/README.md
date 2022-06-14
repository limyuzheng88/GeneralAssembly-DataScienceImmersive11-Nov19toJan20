# Capstone Project: End-to-End Marketing Strategy for E-commerce & Traditional Retail
In your business, would you like to raise revenue, and cut costs? Here, I offer an end-to-end marketing strategy to achieve that using Data Science, by sifting out high/low-value customers (thereby adopting different marketing strategies on them), offering personalised product recommendations to them, and keeping them continuously engaged.
## Summary:

Project encompasses: 1. Customer Segmentation, 2. Personalised product recommendations, 3. Email Marketing Campaign for continued customer engagement, as described below...

1. I segmented my customers into different clusters (via Kmeans, RFM) to deliver tailored marketing strategies. I created a marketing dashboard (on Tableau Public), to provide management with insights on business analytics, and to prescribe recommendations on how best to target each customer/customer segment. 

  Dashboard here (expand full screen for best experience): https://public.tableau.com/profile/lim.yu.zheng#!/vizhome/UCI-retail-recommenderMarketing-Dashboard/Story1?publish=yes

2. I then serve personalised product recommendations (via Collaborative Filtering with implicit feedback; Market Basket Analysis) to my customers, on an e-commerce website that I created on Heroku.

  Website here: http://uci-retail-recommender.herokuapp.com/

3. Finally, for continued customer engagement, I ran an email marketing campaign with A/B testing, to enable the sending of marketing emails for complementary products (via Market Basket Analysis), to targeted customer segments from step 1. 

## Dataset:
UCI Retail Dataset
542k rows: https://archive.ics.uci.edu/ml/datasets/online+retail (used for this project), or 
1.07m rows: https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

## Business Problems:
1. Customer segmentation: 
How can we _**segment customers**_, into different clusters, so as to _**deliver tailored marketing strategies**_, so as to _**minimise promotional costs/retain loyal customers/raise revenue**_?

2. Product Recommendation: 
How can we also _**make personalised product recommendations**_, so as to _**raise revenue**_?

3. Continued customer engagement: 
How can we FURTHER _**engage customers through email/promotion campaigns**_, so as to _**raise revenue**_?

## Conclusions & Recommendations:
### 1. Customer Segmentation:
Best way to segment customers is via Kmeans (5 clusters, silhouette score 0.58). Clusters have been ranked relative to each other in terms of their median RFM, into RFM groups. Tailored marketing strategy for each cluster has been recommended as per https://www.barilliance.com/rfm-analysis/#tab-con-1 . Refer to Jupyter notebook/slides.

**Deployment**

Marketing Dashboard, with marketing strategy for each cluster, and data visualisations for business analytics, has been deployed here (expand to full screen for best experience): https://public.tableau.com/profile/lim.yu.zheng#!/vizhome/UCI-retail-recommenderMarketing-Dashboard/Story1?publish=yes

### 2. Product Recommendation:
Collaborative filtering using the LightFM library was used. Best model ('WARP' loss function, 200 latent features, 'adadelta' learning schedule) achieved mean precision @k=10 is 88% (& mean recall @k=10 is 51%, mean AUC=100%). 

**Deployment**

Mock e-commerce website with collaborative-filtering recommendation engine, and Market Basket Analysis recommendations:  
http://uci-retail-recommender.herokuapp.com/

### 3. Continued customer engagement:
Apriori algorithm was used for Market Basket Analysis, of the dataset. See 'data_rfm_kmeansclusters.csv' for the generated list of highly associated products. For use in email/marketing campaigns (AND on e-commerce website too) to bundle product recommendations together.

**Deployment**

Mock email marketing campaign was launched using Heroku's 'Sendgrid Marketing Campaigns' add-on (campaign control page is accessed by my id & pswd, not shareable).
MBA product associations have been deployed on the mock e-commerce website as well, to be served as 'Customers who bought this also bought that' recommendations, on the 'Checkout' page.

