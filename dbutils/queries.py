sql_query = '''
            insert into
        youtube_results (
            video_id,
            video_publish_date,
            video_title,
            video_discription,
            video_thumbnail
        )
        select
        temp_youtube_results.video_id as video_id,
        temp_youtube_results.video_publish_date as video_publish_date,
        temp_youtube_results.video_title as video_title,
        temp_youtube_results.video_discription as video_discription,
        temp_youtube_results.video_thumbnail as video_thumbnail
        from
        temp_youtube_results
        where
        temp_youtube_results.video_id not in (
            select
            video_id
            from
            youtube_results
        );
'''