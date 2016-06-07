package org.apache.lucene.analysis.standard;

import java.io.IOException;
import java.io.StringReader;
import java.util.Iterator;
import java.io.File;
import java.io.FileReader;

import java.io.FileReader;
import java.util.Iterator;
 
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.FieldType;
import org.apache.lucene.document.StringField; 
import org.apache.lucene.document.TextField; 
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;

/*
 * Author: Xiang Shawn Li
 * This homework is done by following tutorial from UCLA
 * Reference link: http://oak.cs.ucla.edu/cs144/projects/lucene/
 */

public class hw3_Q3_index {
	public hw3_Q3_index() {
    }
 
    private IndexWriter indexWriter = null;
    
    public IndexWriter getIndexWriter(boolean create) throws IOException {
        if (indexWriter == null) {
            Directory indexDir = FSDirectory.open(new File("index-directory"));
            IndexWriterConfig config = new IndexWriterConfig(Version.LUCENE_4_10_2, new StandardAnalyzer());
            indexWriter = new IndexWriter(indexDir, config);
        }
        return indexWriter;
   }    
   
    public void closeIndexWriter() throws IOException {
        if (indexWriter != null) {
            indexWriter.close();
        }
   }
    
    public void indexing(JSONObject metrics, String key) throws IOException {
    	
    	JSONObject content = (JSONObject)metrics.get(key);
  	  	String[] parts = key.split("_");
        String country_descri = (String) content.get("country");
        String capital_descri = (String) content.get("city");
        
        System.out.println("Indexing city_country: " + key);
        IndexWriter writer = getIndexWriter(false);
        Document doc = new Document();
		doc.add(new TextField("city_name", parts[0], Field.Store.YES));
		doc.add(new TextField("country_name", parts[1], Field.Store.YES));
		//doc.add(new TextField("country_text", country_descri, Field.Store.YES));
		//doc.add(new TextField("city_text", capital_descri, Field.Store.YES));
		
		FieldType type = new FieldType();
		type.setIndexed(true);
		type.setStored(true);
		type.setStoreTermVectors(true); //TermVectors are needed for MoreLikeThi

		doc.add(new Field("city_text", capital_descri, type));
		doc.add(new Field("country_text", country_descri, type));
		
		
        writer.addDocument(doc);
    }   
    
    public void rebuildIndexes(String jsonFileName) throws IOException {
        //
        // Erase existing index
        //
        getIndexWriter(true);
        //
        // Index all entries
        //
        JSONParser parser = new JSONParser();
        try {
      	  Object obj = parser.parse(new FileReader(jsonFileName));
      	  
      	  JSONObject jsonObject = (JSONObject) obj;
            
            for(Iterator iterator = jsonObject.keySet().iterator(); iterator.hasNext();) {
                String key = (String) iterator.next();
                indexing(jsonObject, key);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
            //
        // Don't forget to close the index writer when done
        //
        closeIndexWriter();
   }   
}