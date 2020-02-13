## Business Statement
We are tasked with creating a regression model based on the Ames Housing Dataset. This model will predict the price of a house at sale.

1. As a property agent/real estate agency, which houses should we focus our efforts on selling, to yield the best sales/commission? Which should we avoid?  

2. Can we build a model to accurately predict the saleprice of a house, to become The Authority in house saleprices which house buyers can turn to?

## Data Description of given datasets' features are as follows:
http://jse.amstat.org/v19n3/decock/DataDocumentation.txt

## Conclusion

I. VIF_chi2_ridge_optimal model works best (R2 = 0.9039, kaggle score 30227), significantly better than the linreg baseline score (R2 = 0.779, kaggle score = 1067149275989930). 

II. Best 10 features affecting saleprices (best to least best), hence focus our efforts on selling houses which have these features:

    1. 'Neighborhood   = NoRidge'
    2. 'Roof Matl      = WdShngl'
    3. 'Neighborhood   = StoneBr'
    4. 'Garage Qual    = Gd'
    5. Large 'Total Bsmt SF' 
    6. 'Kitchen Qual   = Ex'
    7. 'Exter Qual     = Ex'
    8. 'Garage Type    = BuiltIn'
    9. 'Neighborhood   = NridgHt'
    10. 'Bsmt Exposure = Gd'
       
III. Worst 10 features affecting saleprices (worst to least worst), hence avoid selling houses which have these features:

    1. 'Functional    = Sal'
    2. 'Heating QC    = Po'
    3. 'MS Zoning     = A (agr)'
    4. 'Exter Qual    = TA'
    5  'Heating       = Grav' 
    6. Small 'Bsmt Unf SF'
    7. 'Bsmt Qual     = Gd'
    8. 'Kitchen Qual  = TA'
    9. 'Neighborhood  = Gilbert'
    10. 'Neighborhood = OldTown'
