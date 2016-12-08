package com.example.spiderrobot;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Switch;
import android.widget.Toast;
import android.widget.ToggleButton;

import com.example.spiderrobot.R;

public class MainActivity extends Activity {
	
    private Button startService;  
    private Switch toggleBtn1;
    private Button btn1;
    private WebView web;
    private EditText ev;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		toggleBtn1 = (Switch) findViewById(R.id.toggleButton1);
		btn1 = (Button) findViewById(R.id.btn1);
		web = (WebView) findViewById(R.id.wv);
		web.setWebViewClient(new WebViewClient());
		WebSettings websetting = web.getSettings();
		websetting.setJavaScriptEnabled(true);
		web.getSettings().setUseWideViewPort(true);
		web.getSettings().setLoadWithOverviewMode(true);
		ev = (EditText) findViewById(R.id.ev);
//        startService = (Button) findViewById(R.id.start_service);  
//        stopService = (Button) findViewById(R.id.stop_service);  
//        startService.setOnClickListener(this);  
//        stopService.setOnClickListener(this);  
		btn1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				web.loadUrl(ev.getText().toString());
			}
		});
        toggleBtn1.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
		        if (toggleBtn1.isChecked()) {   
		            Intent startIntent = new Intent(MainActivity.this, MyService.class);  
		            startService(startIntent);  
		            Toast.makeText(MainActivity.this, "通知開啟中", Toast.LENGTH_SHORT).show(); 	
		        }else { 
		            Intent stopIntent = new Intent(MainActivity.this, MyService.class);  
		            stopService(stopIntent);
		            Toast.makeText(MainActivity.this, "通知關閉中", Toast.LENGTH_SHORT).show();          
		            }
			}
		});
	}
/*	
	@Override
	public void onClick(View v) {
		// TODO Auto-generated method stub
        switch (v.getId()) {  
        case R.id.start_service:  
            Intent startIntent = new Intent(this, MyService.class);  
            startService(startIntent);  
            break;  
        case R.id.stop_service:  
            Intent stopIntent = new Intent(this, MyService.class);  
            stopService(stopIntent);  
            break;  
        default:  
            break;  
        } 
  
    }  
*/

}
