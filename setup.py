from distutils.core import setup
import sys
from os.path import join

p1 = str(sys.version_info[0])
p2 = str(sys.version_info[1])

site_package = "lib/python" + p1 + "." + p2 + "/site-packages/mocap"

setup(
    name="mocap",
    version="1.2.42",
    packages=[
        "mocap",
        "mocap/datasets",
        "mocap/datasets/amass_constants",
        "mocap/visualization",
        "mocap/math",
        "mocap/mlutil",
        "mocap/evaluation",
        "mocap/processing",
        "mocap/dataaquisition",
    ],
    data_files=[
        (
            join(site_package, "data/cmu_eval/train/directing_traffic"),
            [
                "mocap/data/cmu_eval/train/directing_traffic/directing_traffic_3.txt",
                "mocap/data/cmu_eval/train/directing_traffic/directing_traffic_5.txt",
                "mocap/data/cmu_eval/train/directing_traffic/directing_traffic_4.txt",
                "mocap/data/cmu_eval/train/directing_traffic/directing_traffic_2.txt",
                "mocap/data/cmu_eval/train/directing_traffic/directing_traffic_1.txt",
            ],
        ),
        (
            join(site_package, "data/cmu_eval/train/jumping"),
            [
                "mocap/data/cmu_eval/train/jumping/jumping_2.txt",
                "mocap/data/cmu_eval/train/jumping/jumping_3.txt",
                "mocap/data/cmu_eval/train/jumping/jumping_1.txt",
                "mocap/data/cmu_eval/train/jumping/jumping_4.txt",
                "mocap/data/cmu_eval/train/jumping/jumping_5.txt",
            ],
        ),
        (
            join(site_package, "data/cmu_eval/train/basketball_signal"),
            [
                "mocap/data/cmu_eval/train/basketball_signal/basketball_signal_5.txt",
                "mocap/data/cmu_eval/train/basketball_signal/basketball_signal_4.txt",
                "mocap/data/cmu_eval/train/basketball_signal/basketball_signal_2.txt",
                "mocap/data/cmu_eval/train/basketball_signal/basketball_signal_1.txt",
                "mocap/data/cmu_eval/train/basketball_signal/basketball_signal_3.txt",
            ],
        ),
        (
            join(site_package, "data/cmu_eval/train/walking"),
            [
                "mocap/data/cmu_eval/train/walking/walking_2.txt",
                "mocap/data/cmu_eval/train/walking/walking_5.txt",
                "mocap/data/cmu_eval/train/walking/walking_1.txt",
                "mocap/data/cmu_eval/train/walking/walking_4.txt",
                "mocap/data/cmu_eval/train/walking/walking_3.txt",
            ],
        ),
        (
            join(site_package, "data/cmu_eval/train/washwindow"),
            [
                "mocap/data/cmu_eval/train/washwindow/washwindow_5.txt",
                "mocap/data/cmu_eval/train/washwindow/washwindow_1.txt",
                "mocap/data/cmu_eval/train/washwindow/washwindow_3.txt",
                "mocap/data/cmu_eval/train/washwindow/washwindow_2.txt",
                "mocap/data/cmu_eval/train/washwindow/washwindow_4.txt",
            ],
        ),
        (
            join(site_package, "data/cmu_eval/train/basketball"),
            [
                "mocap/data/cmu_eval/train/basketball/basketball_4.txt",
                "mocap/data/cmu_eval/train/basketball/basketball_1.txt",
                "mocap/data/cmu_eval/train/basketball/basketball_5.txt",
                "mocap/data/cmu_eval/train/basketball/basketball_3.txt",
                "mocap/data/cmu_eval/train/basketball/basketball_2.txt",
            ],
        ),
        (
            join(site_package, "data/cmu_eval/train/running"),
            [
                "mocap/data/cmu_eval/train/running/running_3.txt",
                "mocap/data/cmu_eval/train/running/running_1.txt",
                "mocap/data/cmu_eval/train/running/running_5.txt",
                "mocap/data/cmu_eval/train/running/running_2.txt",
                "mocap/data/cmu_eval/train/running/running_4.txt",
            ],
        ),
        (
            join(site_package, "data/cmu_eval/train/soccer"),
            [
                "mocap/data/cmu_eval/train/soccer/soccer_3.txt",
                "mocap/data/cmu_eval/train/soccer/soccer_4.txt",
                "mocap/data/cmu_eval/train/soccer/soccer_2.txt",
                "mocap/data/cmu_eval/train/soccer/soccer_5.txt",
                "mocap/data/cmu_eval/train/soccer/soccer_1.txt",
            ],
        ),
        (
            join(site_package, "data/cmu_eval/train/walking_extra"),
            [
                "mocap/data/cmu_eval/train/walking_extra/walking_41.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_30.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_46.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_14.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_23.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_36.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_22.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_21.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_13.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_49.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_40.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_20.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_48.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_25.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_32.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_43.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_38.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_37.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_47.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_27.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_35.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_51.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_28.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_45.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_39.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_33.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_18.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_44.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_24.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_19.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_31.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_26.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_29.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_52.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_50.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_42.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_15.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_34.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_16.txt",
                "mocap/data/cmu_eval/train/walking_extra/walking_17.txt",
            ],
        ),
        (
            join(site_package, "data/cmu_eval/test/directing_traffic"),
            ["mocap/data/cmu_eval/test/directing_traffic/directing_traffic_1.txt"],
        ),
        (
            join(site_package, "data/cmu_eval/test/jumping"),
            ["mocap/data/cmu_eval/test/jumping/jumping_1.txt"],
        ),
        (
            join(site_package, "data/cmu_eval/test/basketball_signal"),
            ["mocap/data/cmu_eval/test/basketball_signal/basketball_signal_1.txt"],
        ),
        (
            join(site_package, "data/cmu_eval/test/walking"),
            ["mocap/data/cmu_eval/test/walking/walking_1.txt"],
        ),
        (
            join(site_package, "data/cmu_eval/test/washwindow"),
            ["mocap/data/cmu_eval/test/washwindow/washwindow_1.txt"],
        ),
        (
            join(site_package, "data/cmu_eval/test/basketball"),
            ["mocap/data/cmu_eval/test/basketball/basketball_1.txt"],
        ),
        (
            join(site_package, "data/cmu_eval/test/running"),
            ["mocap/data/cmu_eval/test/running/running_1.txt"],
        ),
        (
            join(site_package, "data/cmu_eval/test/soccer"),
            ["mocap/data/cmu_eval/test/soccer/soccer_1.txt"],
        ),
        (
            join(site_package, "data/cmu_eval/test/walking_extra"),
            [
                "mocap/data/cmu_eval/test/walking_extra/walking_9.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_14.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_23.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_22.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_10.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_21.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_13.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_20.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_7.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_6.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_18.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_11.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_19.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_8.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_15.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_16.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_12.txt",
                "mocap/data/cmu_eval/test/walking_extra/walking_17.txt",
            ],
        ),
        (
            join(site_package, "data/amass"),
            [
                "mocap/data/amass/test_fnames.txt",
                "mocap/data/amass/training_fnames.txt",
                "mocap/data/amass/validation_fnames.txt",
            ],
        ),
        (
            join(site_package, "data/h36m/labels"),
            [
                "mocap/data/h36m/labels/S9_walkingdog_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_purchases_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_discussion_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_takingphoto_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_smoking_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_directions_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_phoning_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_smoking_2_label.txt.zip",
                "mocap/data/h36m/labels/S5_walkingtogether_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_phoning_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_directions_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_posing_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_smoking_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_walking_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_greeting_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_purchases_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_sitting_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_directions_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_greeting_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_eating_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_directions_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_waiting_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_phoning_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_sittingdown_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_greeting_2_label.txt.zip",
                "mocap/data/h36m/labels/S5_directions_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_sittingdown_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_walking_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_takingphoto_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_sitting_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_phoning_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_directions_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_takingphoto_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_eating_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_waiting_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_directions_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_sittingdown_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_waiting_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_walkingdog_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_walkingdog_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_walking_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_smoking_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_walkingtogether_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_posing_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_discussion_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_posing_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_directions_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_sittingdown_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_takingphoto_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_posing_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_smoking_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_sitting_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_sittingdown_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_takingphoto_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_sitting_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_purchases_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_walkingtogether_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_takingphoto_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_posing_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_discussion_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_posing_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_directions_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_directions_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_takingphoto_2_label.txt.zip",
                "mocap/data/h36m/labels/S5_greeting_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_discussion_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_greeting_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_walking_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_greeting_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_waiting_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_purchases_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_greeting_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_sitting_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_posing_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_directions_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_sitting_2_label.txt.zip",
                "mocap/data/h36m/labels/S5_walkingdog_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_takingphoto_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_discussion_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_smoking_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_eating_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_waiting_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_walkingdog_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_smoking_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_sitting_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_sitting_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_eating_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_takingphoto_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_eating_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_sittingdown_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_discussion_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_purchases_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_takingphoto_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_smoking_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_walking_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_discussion_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_eating_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_waiting_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_takingphoto_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_greeting_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_smoking_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_walking_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_walkingtogether_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_posing_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_walkingtogether_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_purchases_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_walkingtogether_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_eating_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_eating_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_purchases_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_takingphoto_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_waiting_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_walkingtogether_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_waiting_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_discussion_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_sitting_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_waiting_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_sitting_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_waiting_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_eating_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_purchases_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_purchases_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_walkingdog_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_smoking_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_takingphoto_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_purchases_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_sittingdown_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_walkingdog_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_discussion_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_posing_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_walkingtogether_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_walkingdog_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_sitting_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_phoning_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_phoning_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_walking_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_sittingdown_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_waiting_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_posing_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_sittingdown_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_discussion_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_discussion_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_walking_2_label.txt.zip",
                "mocap/data/h36m/labels/S5_walking_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_walking_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_sittingdown_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_walking_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_eating_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_greeting_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_walkingtogether_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_phoning_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_waiting_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_greeting_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_greeting_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_sitting_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_greeting_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_sittingdown_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_directions_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_sittingdown_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_phoning_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_eating_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_directions_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_discussion_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_posing_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_smoking_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_smoking_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_smoking_2_label.txt.zip",
                "mocap/data/h36m/labels/S5_phoning_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_walkingtogether_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_walkingtogether_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_eating_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_walkingtogether_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_purchases_2_label.txt.zip",
                "mocap/data/h36m/labels/S5_takingphoto_1_label.txt.zip",
                "mocap/data/h36m/labels/S9_phoning_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_sitting_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_sittingdown_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_greeting_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_posing_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_walkingdog_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_discussion_1_label.txt.zip",
                "mocap/data/h36m/labels/S8_eating_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_walkingdog_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_walkingdog_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_greeting_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_waiting_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_purchases_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_waiting_2_label.txt.zip",
                "mocap/data/h36m/labels/S5_phoning_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_walkingdog_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_purchases_2_label.txt.zip",
                "mocap/data/h36m/labels/S1_phoning_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_posing_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_directions_1_label.txt.zip",
                "mocap/data/h36m/labels/S1_sitting_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_walkingtogether_2_label.txt.zip",
                "mocap/data/h36m/labels/S8_eating_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_smoking_2_label.txt.zip",
                "mocap/data/h36m/labels/S6_walking_1_label.txt.zip",
                "mocap/data/h36m/labels/S11_walking_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_walkingtogether_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_phoning_1_label.txt.zip",
                "mocap/data/h36m/labels/S5_purchases_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_posing_1_label.txt.zip",
                "mocap/data/h36m/labels/S6_walkingdog_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_walking_1_label.txt.zip",
                "mocap/data/h36m/labels/S7_discussion_2_label.txt.zip",
                "mocap/data/h36m/labels/S9_sittingdown_2_label.txt.zip",
                "mocap/data/h36m/labels/S7_walkingdog_2_label.txt.zip",
                "mocap/data/h36m/labels/S11_phoning_1_label.txt.zip",
            ],
        ),
    ],
)
