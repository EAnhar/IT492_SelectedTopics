
<html>
    <head>
        <title>All Times and APIs</title>
    </head>

    <body>
        <h1>listAll</h1>
        <ul>
            <?php
            //our url
            $json = file_get_contents('http://api-service/listAll');
            $obj = json_decode($json);
            
            //open and close times from api.py
	          $openTime = $obj->open;
	          $closeTime = $obj->close;
	          
	        //loop through open and close with foreach times and print out via echo
	        echo "	Open:\n";
            foreach ($openTime as $l) {
                echo "<li>$l</li>";
            }
            
            echo "	Close:\n";
            foreach ($closeTime as $l) {
                echo "<li>$l</li>";
            }
        //now we make all of our cases below
            ?>
            
        <h1>listOpenOnly</h1>
            <?php
            $json = file_get_contents('http://api-service/listOpenOnly');
            $obj = json_decode($json);
	          $openTime = $obj->open;
	          
	        echo "	Open:\n";
            foreach ($openTime as $l) {
                echo "<li>$l</li>";
            }
            ?>
        
        <h1>listCloseOnly</h1>
            <?php
            $json = file_get_contents('http://api-service/listCloseOnly');
            $obj = json_decode($json);
	          $closeTime = $obj->close;
	          
	        echo "	Close:\n";
            foreach ($closeTime as $l) {
                echo "<li>$l</li>";
            }
            ?>
          
         <h1>listAllJson</h1>
            <?php
            $json = file_get_contents('http://api-service/listAll/json');
            $obj = json_decode($json);
            
	          $openTime = $obj->open;
	          $closeTime = $obj->close;

	        echo "	Open:\n";
            foreach ($openTime as $l) {
                echo "<li>$l</li>";
            }
            
            echo "	Close:\n";
            foreach ($closeTime as $l) {
                echo "<li>$l</li>";
            }
            
            ?>

         <h1>openOnlyJson</h1>
            <?php
            $json = file_get_contents('http://api-service/listOpenOnly/json');
            $obj = json_decode($json);
            
	          $openTime = $obj->open;
	          
	        echo "	Open:\n";
            foreach ($openTime as $l) {
                echo "<li>$l</li>";
            }
            ?>
            
         <h1>closeOnlyJson</h1>
            <?php
            $json = file_get_contents('http://api-service/listCloseOnly/json');
            $obj = json_decode($json);
            
	          $closeTime = $obj->close;
	          
	        echo "	Close:\n";
            foreach ($closeTime as $l) {
                echo "<li>$l</li>";
            }
            ?>
            
         <h1>Json top 5 (open)</h1>
            <?php
            $json = file_get_contents('http://api-service/listOpenOnly/json?top=5');
            $obj = json_decode($json);
            
	          $openTime = $obj->open;
	          
	        echo "	Top 5 Open:\n";
            foreach ($openTime as $l) {
                echo "<li>$l</li>";
            }
            ?>
            
         <h1>Json top 4 (close)</h1>
            <?php
            $json = file_get_contents('http://api-service/listCloseOnly/json?top=4');
            $obj = json_decode($json);
            
	          $closeTime = $obj->close;
	          
	        echo "	Top 4 Close:\n";
            foreach ($closeTime as $l) {
                echo "<li>$l</li>";
            }
            ?>
          
        <h1>listAllCsv</h1>
            <?php
            echo file_get_contents('http://api-service/listAll/csv');
            ?>
            
        <h1>openOnlyCsv</h1>
            <?php
            echo file_get_contents('http://api-service/listOpenOnly/csv');
            ?>
            
        <h1>closeOnlyCsv</h1>
            <?php
            echo file_get_contents('http://api-service/listCloseOnly/csv');
            ?>
            
        <h1>Csv top 3 (Open)</h1>
            <?php
            echo file_get_contents('http://api-service/listOpenOnly/csv?top=3');
            ?>
         
        <h1>Csv top 6 (Close)</h1>
            <?php
            echo file_get_contents('http://api-service/listCloseOnly/csv?top=6');
            ?>
  
            
        </ul>
    </body>
</html>