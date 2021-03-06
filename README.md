# RedditSync

Based off of https://github.com/antoineclaval/ReddiTwitter, this application will monitor a subreddit and blog all new posts.

## Usage

Before running any scripts, run: `source .secret` to load the API key(s) as environment variables. Also please ensure that `credentials.json` is present in the root directory for Google's credentials.

### Blogger

- **List Blogs**: `python -m redditsync.blogger.list_blogs`
- **List Posts**: `python -m redditsync.blogger.list_posts <blog_id1> <blog_id2>`
- **Create Sample Blog Post**: `python -m redditsync.blogger.create_post`
- **Delete Posts**: `python -m redditsync.blogger.delete_all_posts <blog_id1> <blog_id2>`

### Wordpress

- **List Posts**: `python -m redditsync.wordpress.list_posts`
- **Create Sample Blog Post**: `python -m redditsync.wordpress.create_post`

### Reddit

- **Get Newest Reddit Post**: `python -m redditsync.reddit.get_newest_subreddit_post <subreddit1> <subreddit2>`

### Shorte

- **Shorten URL**: `python -m redditsync.shorten_link <url1> <url2>`

### Main

- **Monitor Subreddit and Post to Blogger and/or Wordpress**: `python -m redditsync.sync`

## Setup

### Provision Server

```
export MYSERVER="104.236.115.219" # DigitalOcean
# export MYSERVER="li1022-36.members.linode.com" # Linode
```

Enable passwordless authentication to remote server.

```
ssh-copy-id root@$MYSERVER
```

SSH Into Server

```
ssh root@$MYSERVER
```

After sshing into the server:

```
curl https://raw.githubusercontent.com/AlJohri/RedditSync/master/provision.sh | bash
```

Push credentials to server:

```
scp .secret root@$MYSERVER:RedditSync/
scp credentials.dat root@$MYSERVER:RedditSync/
scp credentials.json root@$MYSERVER:RedditSync/
```

### Create a Google App from the Developers Console with Blogger API Enabled

https://github.com/AlJohri/RedditSync/blob/master/blogger.md

### Install Dependencies, Set API Keys and Credentials, Configure Subreddits and Blogs

1. Install dependencies: `pip install -r requirements.txt`
2. Move `credentials.json` to root of repository.
3. Create `.secret` file. `cp .secret.example .secret`.
4. Fill in the `.secret` file with the Shorte API key.
5. Modify `input.csv` to includde the desired subreddits and blog ids.

## Sample Output

### List Blogs
```
$ python -m redditsync.blogger.list_blogs
Blogs for User: self

8891791559553249304 Test Blog Coders Clan http://testblogcodersclan.blogspot.com/
7454052228383034242 EECS 345 2013 Distributed Systems http://eecs345-2013.blogspot.com/
```

### List Posts
```
$ python -m redditsync.blogger.list_posts 7454052228383034242
Posts for Blog: 7454052228383034242

3900147049471738877 Where Does the Internet Filtering Occur in China? http://eecs345-2013.blogspot.com/2013/03/where-does-internet-filtering-occur-in.html
1369787067449049009 Tor: The Second-Generation Onion Router http://eecs345-2013.blogspot.com/2013/03/tor-second-generation-onion-router.html
1355651638825712622 The Costs and Limits of Availability of Replicated Services http://eecs345-2013.blogspot.com/2013/03/the-costs-and-limits-of-availability-of.html
8092424664669101545 Practical Byzantine Fault Tolerance http://eecs345-2013.blogspot.com/2013/03/practical-byzantine-fault-tolerance.html
4488200843167442011 Scatter http://eecs345-2013.blogspot.com/2013/03/scatter.html
4228039794435391347 Spanner http://eecs345-2013.blogspot.com/2013/02/spanner.html
...
```

### Shorten URL
```
$ python -m redditsync.shorten_link google.com yahoo.com cnn.com
google.com 	 http://sh.st/QONGW
yahoo.com 	 http://sh.st/QOMZf
cnn.com 	 http://sh.st/QPurB
```
### Get Newest Subreddit Post
```
$ python -m redditsync.reddit.get_newest_subreddit_post datasets dataisbeautiful machinelearning
datasets | 44f508 | eligibleBASc | Felix Baumgartner altitude and speed vs time | https://www.reddit.com/r/datasets/comments/44f508/felix_baumgartner_altitude_and_speed_vs_time/
dataisbeautiful | 44ejmr | jimrosenz | How unrepresentative are the early presidential primary states? | Brookings Institution | http://www.brookings.edu/research/opinions/2016/02/03-early-presidential-primary-states-frey?cid=00900015020089101US0001-02041
machinelearning | 44f4qg | textClassy | is there any high quality research into using deep learning for cognitive augmentation | https://www.reddit.com/r/MachineLearning/comments/44f4qg/is_there_any_high_quality_research_into_using/
```

### Monitor Subreddit and Post to Blogger
```
$ python -m redditsync.monitor_subreddits_and_create_blogposts

-------------------------------------
Found new Submission:  44iucn Bypassing Rolling Systems (like those used on cars) with cheap radio hardware
Found new Submission:  44k2nc Need advice regarding the following Statistics Books
Found new Submission:  43djn7 [OC] Single and Multiple Regression using Python
Found new Submission:  44jd6i Long Short-Term Memory-Networks for Machine Reading
Found new Submission:  44j187 Why is so much Far-right extremism being up-voted to the top of World News?
Found new Submission:  44k7h3 Opinions: Am I doing the right think in my situation buying a new car?
Found new Submission:  44jn3h Trying to find a certain visualization
Found new Submission:  44k7zr Indigenous and non-Indigenous land titling from 1788 in Australia
Found new Submission:  44k7lb Graduate this May, having rejections on resume coming left and right. No internship experience(had to run a family business)
Found new Submission:  44hk9s How to use SymPy as an alternative of Wolfram Alpha and Mathematica
Writing submission [44iucn Bypassing Rolling Systems (like those used on cars) with cheap radio hardware] to blog 3722813601574169641 for subreddit netsec
Writing submission [44k2nc Need advice regarding the following Statistics Books] to blog 8891791559553249304 for subreddit statistics
Writing submission [43djn7 [OC] Single and Multiple Regression using Python] to blog 8891791559553249304 for subreddit pystats
Writing submission [44j187 Why is so much Far-right extremism being up-voted to the top of World News?] to blog 3722813601574169641 for subreddit OutOfTheLoop
Writing submission [44k7h3 Opinions: Am I doing the right think in my situation buying a new car?] to blog 3722813601574169641 for subreddit personalfinance
Writing submission [44jn3h Trying to find a certain visualization] to blog 8891791559553249304 for subreddit datasets
Writing submission [44k7zr Indigenous and non-Indigenous land titling from 1788 in Australia] to blog 8891791559553249304 for subreddit dataisbeautiful
Writing submission [44k7lb Graduate this May, having rejections on resume coming left and right. No internship experience(had to run a family business)] to blog 3722813601574169641 for subreddit cscareerquestions
Writing submission [44hk9s How to use SymPy as an alternative of Wolfram Alpha and Mathematica] to blog 8891791559553249304 for subreddit datascience
Sleeping for 5 minutes...

-------------------------------------
Found new Submission:  44kclf Sonicwall Rule, Group, and Service Parser
Writing submission [44kclf Sonicwall Rule, Group, and Service Parser] to blog 3722813601574169641 for subreddit netsec
Sleeping for 5 minutes...

-------------------------------------
No new submissions found.
Sleeping for 5 minutes...

-------------------------------------
No new submissions found.
Sleeping for 5 minutes...

-------------------------------------
No new submissions found.
Sleeping for 5 minutes...
```
