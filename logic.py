import re


def add_time(hours, hours_add, day=""):
    hour_pattern = r"([0-9]*):([0-9]+) ([p|a|P|A][m|M])"
    hour_add_pattern = r"([0-9]*):([0-9]*)"
    hours = re.findall(hour_pattern, hours)
    hours_add = re.findall(hour_add_pattern, hours_add)
    h = (hours[0][0]).split()
    m = (hours[0][1]).split()
    td = (hours[0][2]).split()
    h_a = (hours_add[0][0]).split()
    m_a = (hours_add[0][1]).split()
    output = [0, 0, ""]
    final = ["", "", "", "", ""]
    day_chart = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for ho, minute, time_of_day, h_add, m_add in zip(h, m, td, h_a, m_a):
        output[1] = int(minute) + int(m_add)
        output[0] = int(ho) + int(h_add)
        if output[1] > 59:
            output[0] += 1
            output[1] -= 60
        if time_of_day.upper() == "PM":
            output[0] += 12
    hours = output[0]
    minutes = output[1]
    if hours < 24:
        if hours <= 12:
            final[0] = "{}".format(hours)
            final[2] = td[0].upper()
            final[3] = day.lower().capitalize()
        else:
            final[0] = "{}".format(hours-12)  # :02d
            if td[0].upper() == "AM":
                final[2] = "AM"
            elif td[0].upper() == "PM":
                final[2] = "PM"
            final[3] = day.lower().capitalize()
        if final[0] == "0":
            final[0] = "12"
    elif td[0].upper() == "AM" and 23 < hours < 36:
        final[0] = "{}".format(hours-24)
        final[2] = "PM"
        final[3] = day.lower().capitalize()
    else:
        next_day = hours//24
        if next_day == 1:
            final[4] = "next day"
        else:
            final[4] = "{} days later".format(next_day)
        try:
            final[3] = day_chart[day_chart.index(day.lower().capitalize())+next_day]
        except ValueError:
            pass
        except IndexError:
            final[3] = day_chart[day_chart.index(day.lower().capitalize()) + next_day%7 - 7]
        final[0] = str(hours % 24)
        final[2] = "AM"
        if (hours % 24) > 12:
            final[0] = str((hours % 24) - 12)
            final[2] = "PM"
    if final[0] == "0":
        final[0] = "12"
    final[1] = "{:02d}".format(minutes)
    final_output = final[0]+":"+final[1]+" "+final[2]
    if final[3] != "":
        final_output += ", {}".format(final[3])
    if final[4] != "":
        final_output += " ({})".format(final[4])
    return final_output


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
