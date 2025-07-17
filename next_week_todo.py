#!/usr/bin/python
# -*- coding: utf8 -*-

import calendar
from datetime import datetime, timedelta

TODO_FILE = 'todo.md'


def get_year_week_number():
    today = datetime.now()
    day = today + timedelta(days=7)

    return {
        "year": day.strftime("%Y"),
        "month": day.strftime("%m"),
        "week": day.isocalendar()[1]
    }


def get_weekly_dates():

    # Define week alias name.
    DAYS_OF_WEEK = ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]

    today = datetime.now()
    day = today + timedelta(days=7)

    # Find the Sunday.
    start_of_week = day - timedelta(days=day.weekday() + 1)

    # Create one list to store "Formatted date, day name".
    weekly_dates = []
    for i in range(7):
        date = start_of_week + timedelta(days=i)
        day_name = DAYS_OF_WEEK[i]
        formatted_date = date.strftime("%m.%d")
        weekly_dates.append({
            "date": formatted_date,
            "day_name": day_name
        })
    return weekly_dates


def view_weekly_todo(weekly_dates, md_content):

    for day in weekly_dates:

        day_name = day["day_name"]
        formatted_date = day["date"]
        md_content += f"\n## {formatted_date} ({day_name})\n"
        md_content += "\n- [ ]\n"

    return md_content


def main():

    # H1.
    #
    ywn = get_year_week_number()
    year_num = ywn["year"]
    month_num = ywn["month"]
    week_num = ywn["week"]

    md_content = f"# Weekly of {year_num}.{week_num}\n"

    # Calendar block.
    #
    tc = calendar.TextCalendar()
    cal = tc.formatmonth(int(year_num), int(month_num))
    md_content += "\n```"
    md_content += cal
    md_content += "```"

    md_content += "\n----\n"

    # Dates block.
    #
    weekly_dates = get_weekly_dates()
    result = view_weekly_todo(weekly_dates, md_content)
    result += "\n"

    print(result)

    # Write result into TODO_FILE.
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        f.write(result)


if __name__ == "__main__":
    main()
