package org.apache.lucene.analysis.standard;


import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;

import org.apache.lucene.document.Field;
import org.apache.lucene.document.Document;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.IndexWriter;

import org.apache.lucene.document.Document;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.TopDocs;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.IndexSearcher;

/*
 * Author: Xiang Shawn Li
 * This homework is done by following tutorial from UCLA
 * Reference link: http://oak.cs.ucla.edu/cs144/projects/lucene/
 */

public class hw3_Q3_mainindex {
    
    /** Creates a new instance of Main */
    public hw3_Q3_mainindex() {
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException, ParseException {
      JSONParser parser = new JSONParser();
      
      try {
    	  /*
    	Object obj = parser.parse(new FileReader(
                  "/Users/apple/Documents/MSiA/Fall 2015/Text analytics/HW/hw3/webscraped_data.json"));
          	
	    JSONObject jsonObject = (JSONObject) obj;
	    */
	// build a lucene index
        System.out.println("rebuildIndexes");
        hw3_Q3_index  indexer = new hw3_Q3_index();
        indexer.rebuildIndexes("/Users/apple/Documents/MSiA/Fall 2015/Text analytics/HW/hw3/webscraped_data.json");
        System.out.println("rebuildIndexes done");

      } catch (Exception e) {
        System.out.println("Exception caught.\n");
      }
    }
    
}
