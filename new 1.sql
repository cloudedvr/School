Medical Center Schema Diagram:
  doctors                visits               patients
+-----------+        +-------------+       +-------------+
| doctor_id |◄───────| doctor_id   |       | patient_id  |
| name      |        | patient_id  |──────►| name        |
| specialty |        | visit_id PK |       | contact_info|
+-----------+        | visit_date  |       +-------------+
                     | notes       |
                     +-------------+
                           │
                           ▼
                      diagnoses
                     +-------------+
                     | diagnosis_id|
                     | visit_id    |◄───┐
                     | disease_id  |    │
                     | notes       |    │
                     +-------------+    │
                                         │
                                   diseases
                                  +-------------+
                                  | disease_id  |
                                  | name        |
                                  | description |
                                  +-------------+

--------------------------------------------------

Craigslist Schema Diagram:
             regions
         +-------------+
         | region_id   |
         | name        |
         +-------------+
              ▲        ▲
              |        |
users       posts      |
+----------+  +---------+
| user_id  |  | post_id |
| username |  | title   |
| email    |  | text    |
| pref_reg |  | user_id |────► users
+----------+  | location|
              | region_id|
              +---------+
                   │
                   ▼
             post_categories
              +-------------+
              | post_id     |◄───┐
              | category_id |    │
              +-------------+    │
                                 │
                           categories
                          +-------------+
                          | category_id |
                          | name        |
                          +-------------+

--------------------------------------------------

Soccer League Schema Diagram:
           seasons
       +--------------+
       | season_id    |
       | start_date   |
       | end_date     |
       +--------------+
               │
               ▼
            matches
   +----------------------+
   | match_id             |
   | season_id            |───► seasons
   | match_date           |
   | home_team_id         |────► teams
   | away_team_id         |────► teams
   +----------------------+
             ▲       ▲
             |       |
        teams       teams
   +-------------+ +-------------+
   | team_id     | | team_id     |
   | name        | | name        |
   +-------------+ +-------------+

           players
       +-------------+
       | player_id   |
       | name        |
       | team_id     |────► teams
       +-------------+

           goals
       +-------------+
       | goal_id     |
       | match_id    |────► matches
       | player_id   |────► players
       | goal_time   |
       +-------------+

         referees
       +-------------+
       | referee_id  |
       | name        |
       +-------------+

       match_referees
       +--------------+
       | match_id     |────► matches
       | referee_id   |────► referees
       +--------------+
