package org.apache.lucene.analysis.standard;

import java.io.File;
import java.io.FileReader;
import java.util.Scanner;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.apache.lucene.search.BooleanQuery;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.BooleanClause;
import org.apache.lucene.search.BooleanQuery;
import org.apache.lucene.search.TermQuery;

/*
 * Author: Xiang Shawn Li
 * This homework is done by following tutorial from UCLA
 * Reference link: http://oak.cs.ucla.edu/cs144/projects/lucene/
 */

public class he3_Q4_BoolQuery {
	 /** Creates a new instance of Main */
    public he3_Q4_BoolQuery() {
    }
    
    /**
     * @param args the command line arguments
     */
    
    public static void displayQuery(Query query) {
    	System.out.println("Query: " + query.toString());
    	}

    	
    public static void main(String[] args) {
     
	   
      try {

    	  IndexSearcher is = new IndexSearcher(DirectoryReader.open(FSDirectory.open(new File("index-directory"))));

    	  String FIELD_CONTENTS = "city_text";

    	  Query query1 = new TermQuery(new Term(FIELD_CONTENTS, "greek"));
    	  Query query2 = new TermQuery(new Term(FIELD_CONTENTS, "roman"));
    	  Query query3 = new TermQuery(new Term(FIELD_CONTENTS, "persian"));

    	  BooleanQuery booleanQuery = new BooleanQuery();
    	  booleanQuery.add(query1, BooleanClause.Occur.MUST);
    	  booleanQuery.add(query2, BooleanClause.Occur.MUST);
    	  booleanQuery.add(query3, BooleanClause.Occur.MUST_NOT);
    	  displayQuery(booleanQuery);

    	  TopDocs topDocs = is.search(booleanQuery,249);

        System.out.println("Results found: " + topDocs.totalHits);
        ScoreDoc[] hits = topDocs.scoreDocs;
        for (int i = 0; i < hits.length; i++) {
            Document doc = is.doc(hits[i].doc);
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
