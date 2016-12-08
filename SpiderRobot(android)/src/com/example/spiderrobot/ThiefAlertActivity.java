package com.example.spiderrobot;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.ImageRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.example.spiderrobot.R;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class ThiefAlertActivity extends Activity{
	
	private ImageView img;
	private String str;
	private RequestQueue queue;
	private Button btn2;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		setContentView(R.layout.warning);
		img = (ImageView) findViewById(R.id.img);
		queue = Volley.newRequestQueue(this);
		btn2 = (Button) findViewById(R.id.btn2);
		test1();
		btn2.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				ThiefAlertActivity.this.finish();
			}
		});
	}
	public void test2(){
		ImageRequest request = new ImageRequest(
				"http://172.20.10.3"+str,
			    new Response.Listener<Bitmap>() {
			        @Override
			        public void onResponse(Bitmap bitmap) {
			            img.setImageBitmap(bitmap);
			        }
			    }, 0, 0, null,
			    new Response.ErrorListener() {
			        public void onErrorResponse(VolleyError error) {
			            img.setImageResource(R.drawable.ic_launcher);
			        }
			    });
		queue.add(request);
	}
	
	public void test1(){
		StringRequest stringRequest = 
			new StringRequest(Request.Method.GET, 
					"http://172.20.10.3/single.php", 
					new MyListener(), 
					new MyErrListener());
		queue.add(stringRequest);
	}

	private class MyListener implements Response.Listener<String> {
		@Override
		public void onResponse(String resp) {
			str = resp;
			test2();
		}
	}
	private class MyErrListener implements Response.ErrorListener {
		@Override
		public void onErrorResponse(VolleyError err) {
			
		}
	}
	
}
