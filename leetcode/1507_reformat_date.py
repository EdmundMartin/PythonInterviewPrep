class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }
        split = date.split(" ")
        day = split[0][:-2]
        day = day if len(day) > 1 else f"0{day}"
        output = [split[2], months[split[1]], day]
        return '-'.join(output)


if __name__ == '__main__':
    test_date = "20th Oct 2052"
    result = Solution().reformatDate(test_date)
    assert result == "2052-10-20"

    test_date = "6th Jun 1933"
    result = Solution().reformatDate(test_date)
    assert result == "1933-06-06"

    test_date = "26th May 1960"
    result = Solution().reformatDate(test_date)
    assert result == "1960-05-26"


