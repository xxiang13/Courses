package org.apache.lucene.analysis.standard;

import java.io.File;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.search.FuzzyQuery;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.PhraseQuery;
import org.apache.lucene.search.Query;

/*
 * Author: Xiang Shawn Li
 * This homework is done by following tutorial from UCLA and other online sources
 * Reference link: http://www.tutorialspoint.com/lucene/lucene_fuzzyquery.htm
 */

public class hw3_Q4_FuzzyQuery {
	 /** Creates a new instance of Main */
    public hw3_Q4_FuzzyQuery() {
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

    	  Term term = new Term(FIELD_CONTENTS, "Shakespear");
    	  
    	  FuzzyQuery fuzzyQuery = new FuzzyQuery(term);
    	  
  		  displayQuery(fuzzyQuery);
  		  
  		  TopDocs topDocs = is.search(fuzzyQuery,249);


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
