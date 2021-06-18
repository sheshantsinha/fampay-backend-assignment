# fampay-backend-assignment

## Create virtual environment
`virtualenv fampay-backend -p python3`
## Activate virtual environment
`source fampay-backend/bin/activate`
## Install library
`pip3 install -r requirements.txt`

Mysql Table structure 

Table-1: `youtube_results`

```
+--------------------+--------------+------+-----+---------+-------+
| Field              | Type         | Null | Key | Default | Extra |
+--------------------+--------------+------+-----+---------+-------+
| video_id           | varchar(25)  | NO   | PRI | NULL    |       |
| video_publish_date | datetime     | NO   |     | NULL    |       |
| video_title        | varchar(255) | NO   |     | NULL    |       |
| video_discription  | text         | YES  |     | NULL    |       |
| video_thumbnail    | varchar(255) | NO   |     | NULL    |       |
+--------------------+--------------+------+-----+---------+-------+
```

Table-2: `temp_youtube_results`

```
+--------------------+--------------+------+-----+---------+----------------+
| Field              | Type         | Null | Key | Default | Extra          |
+--------------------+--------------+------+-----+---------+----------------+
| id                 | bigint(20)   | NO   | PRI | NULL    | auto_increment |
| video_id           | varchar(25)  | NO   |     | NULL    |                |
| video_publish_date | datetime     | NO   |     | NULL    |                |
| video_title        | varchar(255) | NO   |     | NULL    |                |
| video_discription  | text         | YES  |     | NULL    |                |
| video_thumbnail    | varchar(255) | NO   |     | NULL    |                |
+--------------------+--------------+------+-----+---------+----------------+
```

# Steps to execute

### 1. copy `setup_template.sh` to `setup.sh`
### 2. execute `source setup.sh`
### 3. Ensure your sql is installed and have an user `youtube` and password `demo1234` or you can change this username and password as per your choice.
### 4. Ensure user has all privileges `GRANT ALL PRIVILEGES ON * . * TO 'youtube'@'localhost'`
### 5. Execute `python3 run.py`
### 6. It will launch on port no. 5000 (probably) `http://localhost:5000/`

# APIs

1. Get pagination results

```
GET /videos/<page-number> 
rtype: {
    "keys": [

    ],
    "result": [

    ]
}
```
Example :-
```
GET /videos/3
rtype: {
    "keys": [
        "id",
        "publishedAt",
        "title",
        "description",
        "thumbnails"
    ],
    "metadata": {
        "record_offset": 20,
        "records_per_page": 10,
        "total_pages": 45
    },
    "result": [
        [
            "2yaFYWRHWwc",
            "Thu, 17 Jun 2021 21:00:01 GMT",
            "18 June 2021 - ICC WTC Final Live,IND vs SL 2021 Match Cancel,IPL 2021 New Update &amp; 6 Big News",
            "My11Circle ...",
            "https://i.ytimg.com/vi/2yaFYWRHWwc/default.jpg"
        ],
        [
            "WeauSw-9WMw",
            "Thu, 17 Jun 2021 20:31:14 GMT",
            "Cricket",
            "Tiktok.",
            "https://i.ytimg.com/vi/WeauSw-9WMw/default.jpg"
        ],
        [
            "6PaKsyBZ494",
            "Thu, 17 Jun 2021 17:33:09 GMT",
            "CRICTALES LIVE CRICKET STREAMING | LIVE DISCUSSION BY WASIF ALI OF TODAY MATCH|IND VS NZ| LHR vs KRK",
            "CRICTALES LIVE CRICKET STREAMING | LIVE DISCUSSION BY WASIF ALI OF TODAY MATCH|IND VS NZ| mul vs que PSL LIVE PSL LIVE MATCH TODAY ...",
            "https://i.ytimg.com/vi/6PaKsyBZ494/default.jpg"
        ],
        [
            "_RaCn6xN39k",
            "Thu, 17 Jun 2021 17:12:01 GMT",
            "LIVE CRICKET DISCUSSION &amp; FAN CHAT OF KARACHI VS LAHORE  - LIVE ANALYSIS OF LQ VS KK  TODAY PSL",
            "psl live today match LIVE CRICKET DISCUSSION & FAN CHAT OF MULTAN vs QUETTA - LIVE ANALYSIS OF ms vs qg TODAY psl live today match LIVE ...",
            "https://i.ytimg.com/vi/_RaCn6xN39k/default.jpg"
        ],
        [
            "REJD-yQ9Qrg",
            "Thu, 17 Jun 2021 16:10:42 GMT",
            "Bedingham Stars With the Bat! | Durham v Lancashire Lightning - Highlights | Vitality Blast 2021",
            "Watch highlights of Durham v Lancashire Lightning at the 2021 Vitality Blast. A super 58 from Durham's David Bedingham led the way for the hosts as they ...",
            "https://i.ytimg.com/vi/REJD-yQ9Qrg/default.jpg"
        ],
        [
            "DcACOvyut1E",
            "Thu, 17 Jun 2021 15:58:50 GMT",
            "Jashan e Cricket | Guest - Nimra Khan | 17th June  2021",
            "JashaneCricket | Guest - #NimraKhan | 17th June 2021 For More Videos Subscribe - https://www.youtube.com/channel/UCF73oBsmZPG6YRZV-vVN1-A Visit ...",
            "https://i.ytimg.com/vi/DcACOvyut1E/default.jpg"
        ],
        [
            "hs24ubdwDf4",
            "Thu, 17 Jun 2021 15:53:24 GMT",
            "Jashan e Cricket | Guest - Nimra Khan | 17th June  2021",
            "JashaneCricket | Guest - #NimraKhan | 17th June 2021 For More Videos Subscribe - https://www.youtube.com/channel/UCF73oBsmZPG6YRZV-vVN1-A Visit ...",
            "https://i.ytimg.com/vi/hs24ubdwDf4/default.jpg"
        ],
        [
            "KTiuwYljg2s",
            "Thu, 17 Jun 2021 14:42:54 GMT",
            "VITALITY BLAST LIVE STREAM | MIDDLESEX V GLOUCESTERSHIRE | 17 JUN 2021",
            "",
            "https://i.ytimg.com/vi/KTiuwYljg2s/default.jpg"
        ],
        [
            "QFfQVWSK_sk",
            "Thu, 17 Jun 2021 14:00:10 GMT",
            "Vitality Blast: Surrey v Sussex",
            "WATCH Surrey take on Sussex   in the Vitality Blast LIVE from The Kia Oval.",
            "https://i.ytimg.com/vi/QFfQVWSK_sk/default.jpg"
        ],
        [
            "lZTX94MO0tE",
            "Thu, 17 Jun 2021 12:55:41 GMT",
            "England v India - Day 2 Highlights | Dunkley Hits 74* On Debut! | Only LV= Insurance Test 2021",
            "Go to ecb.co.uk to join We Are England Cricket Supporters for free and get priority access to tickets and much more! Watch match highlights from Day 2 of the ...",
            "https://i.ytimg.com/vi/lZTX94MO0tE/default.jpg"
        ]
    ]
}
```
2. Get result on the basic of search by title or description

```
GET /videos/search?query=dravid&searchkey=video_title

searchkey = video_title | dvideo_description
rtype: {
    "keys": [

    ],
    "result": [

    ]
}

```

Example:-
```
GET /videos/search?query=Shakib Stars In Huge Chase! | Windies vs Bangladesh - Match Highlights | ICC Cricket World Cup 2019&searchkey=video_title

searchkey = video_title | dvideo_description
rtype: {
    "keys": [
        "id",
        "publishedAt",
        "title",
        "description",
        "thumbnails"
    ],
    "result": [
        [
            "LRtEJPSj2-8",
            "Mon, 17 Jun 2019 12:20:18 GMT",
            "Shakib Stars In Huge Chase! | Windies vs Bangladesh - Match Highlights | ICC Cricket World Cup 2019",
            "Watch full highlights of the West Indies vs Bangladesh match at County Ground, Taunton, Game 23 of the 2019 Cricket World Cup. The home of all the highlights ...",
            "https://i.ytimg.com/vi/LRtEJPSj2-8/default.jpg"
        ]
    ]
}

```

3. Get result on the basic of regex pattern of title or description

```
GET /videos/anon/search?query=sachin
rtype: {
    "keys": [

    ],
    "result": [

    ]
}
```
Example:-
```
GET /videos/anon/search?query=huge
rtype: {
    "keys": [
        "id",
        "publishedAt",
        "title",
        "description",
        "thumbnails"
    ],
    "result": [
        [
            "4RmpQ1fPKh4",
            "Sun, 25 Nov 2018 07:43:15 GMT",
            "Kohli, Krunal secure series-levelling win | Third Gillette T20",
            "Krunal Pandya took four wickets before Virat Kohli built on a fast start by India's openers to steer the tourists home in front of a huge crowd at the SCG.",
            "https://i.ytimg.com/vi/4RmpQ1fPKh4/default.jpg"
        ],
        [
            "LRtEJPSj2-8",
            "Mon, 17 Jun 2019 12:20:18 GMT",
            "Shakib Stars In Huge Chase! | Windies vs Bangladesh - Match Highlights | ICC Cricket World Cup 2019",
            "Watch full highlights of the West Indies vs Bangladesh match at County Ground, Taunton, Game 23 of the 2019 Cricket World Cup. The home of all the highlights ...",
            "https://i.ytimg.com/vi/LRtEJPSj2-8/default.jpg"
        ],
        [
            "ZyZXCs2XGBM",
            "Wed, 12 May 2021 09:15:31 GMT",
            "HUGE Swing! | Stokes, Anderson, Jones &amp; More! | Best Ever Deliveries! | England Cricket",
            "From Caddick to Curran, there's no stopping these big swing deliveries! Find out more at ecb.co.uk This is the official channel of the ECB. Watch all the latest ...",
            "https://i.ytimg.com/vi/ZyZXCs2XGBM/default.jpg"
        ]
    ]
}
```

Docker Image

### 1. Build docker image
    `sudo docker build --tag fam-backend-assignment-app .`
### 2. Run the docker image
    `sudo docker run --name fam-backend-assignment-app -p 5001:5001 fam-backend-assignment-app 

Note:- I was not able to do further steps because i start facing some issue with the sql connector with my laptop;

End:)