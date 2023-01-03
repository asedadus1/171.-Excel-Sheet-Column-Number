def excel_sheet_column_number(column):   
   length = len(column);     
   answer =0;
   i =len(column) -1;
   for index, val in enumerate(column):
      n = ord(val) - 64;
      answer = answer + n * (26 ** i);
      i = i-1;
   return answer;
