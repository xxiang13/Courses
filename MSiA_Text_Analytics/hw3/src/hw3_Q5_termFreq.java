package org.apache.lucene.analysis.standard;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.Terms;
import org.apache.lucene.index.TermsEnum;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.BytesRef;

import java.io.FileWriter;
import java.io.IOException;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

//Reference links
// http://www.sergiy.ca/how-to-iterate-over-a-map-in-java/
// http://stackoverflow.com/questions/20899839/retreiving-values-from-nested-json-object
// http://www.mkyong.com/java/json-simple-example-read-and-write-json/

public class hw3_Q5_termFreq {
	
	 public static void main(String[] args) throws IOException {
		
		 IndexReader reader = DirectoryReader.open(FSDirectory.open(new File("index-directory")));
		 
		 String content = "country_text";
		 String output_name = "termsFreq.json";
		 
		 JSONObject obj = new JSONObject();
		 
		 for (int docId=0; docId < reader.maxDoc(); docId++) {
			 
			 Document doc = reader.document(docId);
			 String city_name = doc.get("city_name");
			 String country_name = doc.get("country_name");
			 String name = city_name + "_" + country_name;
			 
			 Terms vector = reader.getTermVector(docId, content);
			 JSONObject obj_freq = getJsonFreq(vector);
			 obj.put(name, obj_freq );

			 System.out.println("Document " + name + " loaded");
			 
			} 
		 
		 saveToJson(obj, output_name);
		 
	 } 
	 
	 public static JSONObject getJsonFreq(Terms vector) throws IOException{
		 /**
		 * saveToJson
		 * Function write to json file
		 * @param JSONObject obj
		 * @param String fileName 
		 * @throws IOException
		 */
		 
		 JSONObject obj_freq = new JSONObject();
		 
		 TermsEnum termsEnum = null;
		 termsEnum = vector.iterator(termsEnum);
		 
		 BytesRef text = null;
		 while ((text = termsEnum.next()) != null) {
		     String term = text.utf8ToString();
		     int freq = (int) termsEnum.totalTermFreq();
		     
		     obj_freq.put(term, freq);     		     
		 } 

		 return obj_freq;	 	 
	 } 
	 
	 
	 public static void saveToJson(JSONObject obj, String fileName) throws IOException {	 
		/**
		 * saveToJson
		 * Function write to json file
		 * @param JSONObject obj
		 * @param String fileName 
		 * @throws IOException
		 */
		try {
			
			//write json file
			FileWriter file = new FileWriter(fileName);
			file.write(obj.toJSONString());
			file.flush();
			file.close();

		} catch (IOException e) {
			e.printStackTrace();
		}		
		 String workingDir = System.getProperty("user.dir");
		 System.out.println("File " + fileName + " in current working directory : " + workingDir);		 
	 } 

} 
