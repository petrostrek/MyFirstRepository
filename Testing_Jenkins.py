import datetime
now = datetime.datetime.now()
   
fo = open("Testing_Jenkins.txt", "w+")
fo.write( "Hello! First line of testing for jenkins.\n");
fo.write( "2nd line of testing for jenkins.\n");
fo.write( str(now) + "\n");
fo.write( str(now) + "\n");
fo.write( str(now) + "\n");
fo.write( str(now) + "\n");
fo.write( str(now) + "\n");
fo.write( str(now) + "\n");

fo.close()
