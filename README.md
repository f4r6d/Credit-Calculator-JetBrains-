Description
Finally, let's add the ability to compute differentiated payment. This is a kind of payment where the part for reducing the credit principal is constant. Another part of the payment is for interest repayment and it reduces during the credit term. It means that the payment is different every month. Let’s look at the formula:

D_m = \dfrac{P}{n} + i * \left( P - \dfrac{P*(m-1)}{n} \right)D 
m
​	
 = 
n
P
​	
 +i∗(P− 
n
P∗(m−1)
​	
 )

Where:

D_mD 
m
​	
  = mth differentiated payment;

PP = credit principal;

ii = nominal interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01;

nn = number of payments (months);

mm = current period.

As you can see, the user has to input a lot of parameters. So, it might be convenient to use command-line arguments.

Suppose you used to run your credit calculator via a command line like this:

python creditcalc.py
Using command-line arguments, you can run your program this way:

python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
In that case, your program can get different values without asking the user to input them. It can be useful when you are developing your program and trying to find a mistake, so you run the program again and again with the same parameters. Also, it's convenient if you made a mistake in a single parameter. You don't have to input all other values again.

To confidently work with command-line arguments in Python, check out this tutorial.

Objectives
In this stage, you need to implement the following features:

Calculating differentiated payment. To do this, the user may run the program specifying the interest, the number of periods, and the credit principal.
The ability to calculate the same values as in the previous stage for annuity payment (principal, count of periods, and the value of payment). The user specifies all the known parameters using command-line arguments, so there will be one unknown parameter. This is the value that the user wants to calculate.

Handling invalid parameters. It's a good idea to show an error message Incorrect parameters if the parameters are invalid.

The final version of your program is supposed to work from the command line and parse the following parameters:

--type, which indicates the type of payment: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff", or not specified at all, show the error message.
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters
--payment, which refers to the monthly payment. For --type=diff, the payment is different each month, so we cannot calculate a number of periods or the principal, therefore, its combination with --payment is invalid, too:
> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
--principal is used for calculating both types of payment. You can get its value knowing the interest, the annuity payment, and the number of periods.
--periods parameter denotes the number of months and/or years needed to repay the credit. It's calculated based on the interest, annuity payment, and the principal.
--interest is specified without the percentage sign. Note that it may accept a floating-point value. Our credit calculator can't calculate the interest, so these parameters are incorrect:
> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
You might have noticed that for differentiated payments you need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (missing either a number of periods, the payment, or the principal). Thus, when less than four parameters are given, you should display the error message:

> python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters
Another case when you should output this message is with negative values. We can't work with these!

> python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters
Finally, don't forget to compute the value of overpayment, and you'll have your real functional credit calculator!

Examples
The greater-than symbol followed by a space (> ) represent the user input. Note that these are not part of the input.

Example 1: calculating differentiated payments

> python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837
In this example, the user wants to take a credit loan with differentiated payments. You know the principal, the number of periods, and the interest rate, which are 1,000,000, 10 months, and 10%, respectively.

The calculator should calculate the payments for all 10 months. Let’s use the formula mentioned above. In this case:

P = 1000000P=1000000
n = 10n=10
i = \dfrac{ interest }{ 12 * 100\% } = \dfrac { 10\% }{12 * 100\% } = 0.008333...i= 
12∗100%
interest
​	
 = 
12∗100%
10%
​	
 =0.008333...

Then, let’s find the payment for the first month (m=1m=1):

D_1 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(1-1) }{ 10 } \right) = 108333.333...D 
1
​	
 = 
n
P
​	
 +i∗(P− 
n
P∗(m−1)
​	
 )= 
10
1000000
​	
 +0.008333...∗(1000000− 
10
1000000∗(1−1)
​	
 )=108333.333...

The second month (m = 2m=2):

D_2 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(2-1) }{ 10 } \right) = 107500D 
2
​	
 = 
n
P
​	
 +i∗(P− 
n
P∗(m−1)
​	
 )= 
10
1000000
​	
 +0.008333...∗(1000000− 
10
1000000∗(2−1)
​	
 )=107500

The third month (m = 3m=3):

D_3 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(3-1) }{ 10 } \right) = 106666.666...D 
3
​	
 = 
n
P
​	
 +i∗(P− 
n
P∗(m−1)
​	
 )= 
10
1000000
​	
 +0.008333...∗(1000000− 
10
1000000∗(3−1)
​	
 )=106666.666...

And so on. You can see other monthly payments above.

Your credit calculator should output monthly payments for every month like in the first stage. Also, don't forget to round up the floating-point values.
Finally, your credit calculator should add up all the payments and subtract the credit principal so that you get the overpayment.

Example 2: finding the annuity payment for the 60-month (or 5-year) credit loan with the principal 1,000,000 and a 10% interest

> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880
Example 3: less than four arguments are given

> python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.
Example 4: calculating differentiated payments given the principal 500,000, the period of 8 months, and an interest rate of 7.8%

> python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907

Overpayment = 14628
Example 5: calculating the principal for an individual paying 8,722 per month for 120 months (10 years) with an interest rate of 5.6%

> python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your credit principal = 800018!
Overpayment = 246622
Example 6: figuring out how much time an individual needs to repay the credit loan with the principal 500,000, the monthly payment of 23,000 at a 7.8% interest rate

> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this credit!
Overpayment = 52000
