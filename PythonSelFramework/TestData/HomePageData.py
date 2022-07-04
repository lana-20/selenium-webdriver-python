from TestData.excelDemo import sheet


class HomePageData:

    test_HomePage_Data = [{"firstname": "Dagny", "lastname": "Taggart", "gender": "Female"},
                            {"firstname": "Hank", "lastname": "Rearden", "gender": "Male"}]

    @staticmethod
    def getTestData(test_case_name):
        Dict = {}
        # book = openpyxl.load_workbook("/Users/lanabegunova/Downloads/PythonDemo.xlsx")
        # sheet = book.active
        for i in range(1, sheet.max_row + 1):  # get rows
            if sheet.cell(row=i, column=1).value == test_case_name:
                for j in range(2, sheet.max_column + 1):  # get columns
                    #  Dict["lastname"] = "Taggart"
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
        return[Dict]