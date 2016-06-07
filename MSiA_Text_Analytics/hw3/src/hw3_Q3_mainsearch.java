package org.apache.lucene.analysis.standard;

import java.io.FileReader;
import java.util.Scanner;

import org.apache.lucene.document.Document;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.apache.lucene.search.BooleanQuery;

/*
 * Author: Xiang Shawn Li
 * This homework is done by following tutorial from UCLA
 * Reference link: http://oak.cs.ucla.edu/cs144/projects/lucene/
 */

public class hw3_Q3_mainsearch {
	 /** Creates a new instance of Main */
    public hw3_Q3_mainsearch() {
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
     
    	String input = "Shakespear";
	   
      try {

        // and retrieve the top 100 result
        System.out.println("performSearch");
        hw3_Q3_search se = new hw3_Q3_search();
        TopDocs topDocs = se.performSearch(input, 100);

        System.out.println("Results found: " + topDocs.totalHits);
        ScoreDoc[] hits = topDocs.scoreDocs;
        for (int i = 0; i < hits.length; i++) {
            Document doc = se.getDocument(hits[i].doc);
            System.out.println(doc.get("city_name")+","+doc.get("country_name")
                               + " "
                               + " (" + hits[i].score + ")");

        }
        System.out.println("performSearch done");
      } catch (Exception e) {
        System.out.println("Exception caught.\n");
      }
    }
    
}
