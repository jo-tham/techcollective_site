Title: Test draft.tech-collective.com
Date: 2016-06-21 19:15
Slug: test-draft
Authors: Jotham Apaloo
Email: jothamapaloo@gmail.com
Summary: Added a way to see a post that's not merged to master

It's much nicer to see our draft posts on the actual site.

Now, we can! I hope...

I added a record set to AWS Route 53 hosted zone for tech-collective.com. 
The record set is the alias [draft.tech-collective.com](http://draft.tech-collective.com). 
It points to a separate s3 bucket. 

All branches with the prefix `post/` will be run the codeship and deployed to 
the draft s3 bucket.

