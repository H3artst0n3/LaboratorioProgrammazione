class CSVFile:

    def __init__(self, file):
        self.name = file;

    def get_data(self):

        file = open(self.name, "r");

        value = [];
        for line in file:
            element = line.split(",");
            if element[0] != "Date":
                value.append(float(element[1]));
        
        return value;
    pass

obj = CSVFile("shampoo_sales.csv")
print(obj.get_data())