# We can set up sample data sets like this; simulating a select all.
# Will do a join on installation and tehcnician table to display technician name instead of the technician ID.

from datetime import date
# just used date.today() for all dates because didn't want to waste too much time matching datetime format manually.

# sample_installations = [
#     {
#         "installation_id": 1,
#         "technician_name": "Brandi Kuritz",
#         "installation_rating": 4,
#         "installation_date": date.today(),
#         "comment": "Will need an upgrade in 2021."
#     },
#     {
#         "installation_id": 2,
#         "technician_name": "Joo An Choi",
#         "installation_rating": 5,
#         "installation_date": date.today(),
#         "comment": None
#     }
# ]
#
# sample_technicians = [
#     {
#         "technician_id": 1,
#         "first_name": "Brandi",
#         "last_name": "Kuritz",
#         "employee_id": "bdk343942",
#         "start_date": date.today()
# },
#      {
#          "technician_id": 2,
#          "first_name": "Joo An",
#          "last_name": "Choi",
#          "employee_id": "jac838390",
#          "start_date": date.today()
#      }
#
# ]
#
#
# # Will join channels with channel genres to display each channel's genre name and whether it's kid friendly.
# sample_channels = [
#     {
#         "channel_id": 1,
#         "channel_name": "Nickelodeon",
#         "channel_number": 45,
#         "channel_genre": "animation",
#         "kid_friendly": True
# },
#      {
#         "channel_id": 2,
#         "channel_name": "MTV",
#         "channel_number": 70,
#         "channel_genre": "reality",
#         "kid_friendly": False
#      }
#
#  ]
# sample_channel_packages = [
#     {
#         "channel_package_id": 1,
#         "channel_id": 1,
#         "package_id": 2
#     },
#     {
#         "channel_package_id": 2,
#         "channel_id": 2,
#         "package_id": 2
#     },
#     {
#         "channel_package_id": 3,
#         "channel_id": 2,
#         "package_id": 1
#     }
# ]
#
# # Need to change phone number to varchar, int is too small to house phone numbers i think.
# # Should add first and last name to subscriber table.
# # Removing active boolean, or should we?
# sample_subscribers = [
#     {
#         "subscriber_id": 1,
#         "phone_number": 555-555-5555,
#         "postal_code": 91210,
#         "installation_id": 1,
#         "monthly_watch_time": 5540,
#         "age": 34,
#         "gender": "female",
#         "first_name": "Tiffany",
#         "last_name": "Smith"
#     },
#     {
#         "subscriber_id": 2,
#         "phone_number": 555-555-5555,
#         "postal_code": 78705,
#         "installation_id": 2,
#         "monthly_watch_time": 49000,
#         "age": 19,
#         "gender": "male",
#         "first_name": "Richard",
#         "last_name": "Jones"
#     }
# ]
#
# sample_genres = [
#     {
#         "channel_genre_id": 1,
#         "genre_name": "animation",
#         "kid_friendly": True
#     },
#     {
#         "channel_genre_id": 2,
#         "genre_name": "reality",
#         "kid_friendly": False
#     },
#     {
#         "channel_genre_id": 3,
#         "genre_name": "documentary",
#         "kid_friendly": True
#     }
# ]
# # Join to display subscribers first and last name instead of ID, and display package name instead of ID.
# # No need to add that active boolean field, we have subscription status field.
# # Example possible options for this field: ACTIVE, PENDING, CANCELLED, EXPIRED, PAYMENT FAILED, TRIAL, etc.
# sample_susbcriptions = [
#     {
#         "subscription_id": 1,
#         "package_id": "Reality All Day",
#         "subscriber": "Richard Jones",
#         "time_start": date.today(),
#         "last_renewed": date.today(),
#         "subscription_status": "ACTIVE",
#         "premium": False,
#         "subscriber_rating": 3
#     },
#     {
#         "subscription_id": 2,
#         "package_id": "Stars And Beyond",
#         "subscriber": "Tiffany Smith",
#         "time_start": date.today(),
#         "last_renewed": date.today(),
#         "subscription_status": "PENDING",
#         "premium": True,
#         "subscriber_rating": None
#     }
#
# ]
#
#
# # Maybe we could remove time interval and just say all of these are monthly? If we end up doing aggregate functions
# # to answer any questions about revenue, the interval could get annoying. not terrible though, just x52 for weekly,
# # x12 for monthly and x1 for annually.
# sample_packages = [
#     {
#         "package_id": 1,
#         "package_name": "Stars And Beyond",
#         "standard_price": 20.00,
#         "premium_price": 34.00,
#         "time_interval": "month"
#     },
#     {
#         "package_id": 2,
#         "package_name": "Reality All Day",
#         "standard_price": 7.00,
#         "premium_price": 10.00,
#         "time_interval": "week"
#     }
# ]

sample_packages = [[1, "Stars And Beyond", 20.00, 34.00, "month"], [2, "Reality All Day", 7.00, 10.00, "week"]]
sample_installations = [[1, "Brandi Kuritz", 4, date.today(), "hi"], [2, "Joo An Choi", 3, date.today(), "bye"]]
sample_technicians = [[1, "Brandi", "Kuritz", "bdk479478", date.today()], [2, "Joo An", "Choi", "jac484039", date.today()]]
sample_channels = [[1, "Nickelodeon", 45, "animation", True], [2, "MTV", 70, "reality", False]]
sample_channel_packages = [[1, "Nickelodeon", "Reality All Day"], [2, "MTV", "Reality All Day"],
                           [3, "MTV", "Stars And Beyond"]]
sample_subscribers = [[1, "555-555-5555", 91210, 1, 5540, 34, "female", "Tiffany", "Smith"],
                      [2, "555-555-5555", 78705, 2, 49000, 19, "male", "Richard", "Jones"]]
sample_subscriptions = [[1, "Reality All Day", "Richard Jones", date.today(), date.today(), "ACTIVE", False, 3],
                        [2, "Stars And Beyond", "Tiffany Smith", date.today(), date.today(), "PENDING", True, None]]
sample_genres = [[1, "animation", True], [2, "reality", False], [3, "documentary", True]]
