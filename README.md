[![Codeship Status for jo-tham/techcollective_site](https://codeship.com/projects/adbc0860-16e2-0134-793d-3e8c5d75eee7/status?branch=master)](https://codeship.com/projects/158466)

[Add a post to tech-collective.com](https://github.com/jo-tham/techcollective_site/new/master/content/blog)

# Tech Collective

Tech collective is a public monthly meetup base in Whitehorse. Our theme is
everyday problems and solutions relating to technology.

Each meeting, one or more attendees present issues they're facing and how
they've solved them with technology such as a particular app, algorithm,
infrastructure, architecture, programming language, hardware component, etc.

This repository contains the source data for the tech-collective.com website.

It is open, so that members may contribute blog posts and event details.

# Posting
You can make a blog post or edit an event on tech-collective.com right from GitHub!

## Create A Post

To make a blog post the tech-collective.com site click
[here](https://github.com/jo-tham/techcollective_site/new/master/content/blog).

## Name the file

Give the file a name, preferably in the format

`YYYY-MM-DD-yourawesomepost.md`

You can also use `.markdown`, `.mkd`, or `.mdown` in place of `.md`.

## Add Metadata

Each post should have the metadata below, replacing placeholders as appropriate

```
Title: <Your Title>
Date: <YYYY-MM-DD HH:MM>
Slug: <your-title>
Authors: <Your Name>
Email: <youremail@something.com>
Summary: <A summary of your post>
```

Here's an exapmle from an actual post

```
Title: Under Construction
Date: 2016-06-17 10:13
Slug: under-construction
Authors: Jotham Apaloo
Email: jothamapaloo@gmail.com
Summary: Coming Soon
```

## Write A Post

While Pelican supports many file formats for posts, the easiest is to use markdown.

Headers, lists, code blocks, and links should be enough to get you started

```

# Header Level 1
## Header Level 2

-----------------

- item
- another item

-----------------

1. numbered item
2. another numbered item

-----------------

\`\`\` 
x = 10
y = 20
print(x*y)
\`\`\`

----------------

[visible link text](http://actuallink.com/).

```

Additional markdown syntax is available
[here](https://guides.github.com/features/mastering-markdown/) and through the
usual search avenues.

## Publishing Your Post

Once you've authored your post, commit it as a pull request as shown in the
image below

![Image of Pull Request](https://raw.githubusercontent.com/jo-tham/techcollective_site/readme/content/images/publish.png)

# Developing

tech-collective.com is built on the static site generator,
[pelican](http://docs.getpelican.com/en/3.6.3/).

You can customize the [themes](https://github.com/getpelican/pelican-themes/),
and introduce new [plugins](https://github.com/getpelican/pelican-plugins).

To get started

- make sure you have python2.7 and virtualenv installed
- clone this repo
- create the virtualenv
- activate the virtualenv
- install the required packages
- hack away!

For your information, the general structure of the toolchain is given below

![Image of Toolchain](https://raw.githubusercontent.com/jo-tham/techcollective_site/readme/content/images/tech-collective-site-toolchain.png)

# Getting Help & Suggesting Improvements

If you have a problem posting, developing, or using tech-collective.com, or an
idea for improvement, please open an issue on the
[issue tracked](https://github.com/jo-tham/techcollective_site/issues).
