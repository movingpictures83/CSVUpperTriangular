class CSVUpperTriangularPlugin:
    def input(self, filename):
       infile = open(filename, 'r')
       self.colnames = infile.readline().strip().split(',') # Assume rownames=colnames
       self.ADJ  = []
       for line in infile:
          self.ADJ.append(line.strip().split(',')[1:])

    def run(self):
       pass

    def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write("X1,X2,Value\n")
       for i in range(0, len(self.ADJ)):
           for j in range(0, len(self.ADJ[i])):
               if (i < j):
                   outfile.write(self.colnames[i]+","+self.colnames[j]+","+self.ADJ[i][j]+"\n")

