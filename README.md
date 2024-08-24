
# FlaskTelemServer
FlaskTelemServer is a minimal micro service using Flask and Pydantic to accept requests from SausageFileConverter in order to track user usage data.

## Usage data can be used to see:
* Which users haven't yet used the product - Does the product not succesfully solve their problem or is the problem it solves not urgent enough?
* Which users have launched the product but have not yet used it - Is the interface easy enough to navigate?  Are there critical bugs stopping the user from using the product?
* Users who have only used it only a couple of times - Does it not deliver the value which the user expected?  Is the problem only a temporary one?
* Users that are regular and happy - Do these users know other people that could benefit from the product?  Are there features that would make their life even easier?
* Users that use it an insane amount - Are they using your product in a way that you didn't expect?  Are you solving an even bigger problem for them that you hadn't anticipated?

It is important to note however that MAC address and IP Address, when combined, count as PII. In order to collect it under GDPR the user needs to give permission through the privacy policy on a licence agreement.

## Next steps:
The code as written solves the problem as it stood when I wrote it.
However if I were to add another product to my catalog, the next step would be to refactor it and improve the design.  It would have to accept data from multiple products and possibly write to multiple databases. Or even multiple types of database, for example if I decide to switch to Postgres at some point.

I think I would do this by changing the route to a generic '/transactions' url and then fetch a productID from the request.
Then I could either add that as a column in the database, or use a strategy pattern to select the correct database to write the data.

I could also couple to an interface instead of directly to a database to enable switching out different databases.
