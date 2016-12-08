package com.example.spiderrobot;

import java.util.Timer;
import java.util.TimerTask;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.example.spiderrobot.R;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.app.TaskStackBuilder;
import android.content.Intent;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;

public class MyService extends Service{
	private final String url = "http://172.20.10.3/single.php";
    private Timer timer = new Timer();
    private RequestQueue queue;

    private NotificationManager mgr;
    private int nid;
    public String str = "begin";
    

	@Override
	public IBinder onBind(Intent intent) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void onCreate() {
		// TODO Auto-generated method stub
		super.onCreate();
		Log.d("rock", "onCreate()");
        queue = Volley.newRequestQueue(this);

        mgr = (NotificationManager)getSystemService(NOTIFICATION_SERVICE);

	}
    
	@Override
	public int onStartCommand(Intent intent, int flags, int startId) {
		// TODO Auto-generated method stub
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
            StringRequest request = new StringRequest(Request.Method.PUT, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                Log.d("rock",response); 
                try {
                    if(!str.equals(response)){
                    	Log.d("rock","A:"+str);
                    	sendNotice();
                    	str = response;
                    }else{
                    	Log.d("rock","C:"+str);
                    }
				} catch (Exception e) {
					// TODO: handle exception
                	str = response;
                	Log.d("rock","B:"+str);
				}

            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

            }
        });
        queue.add(request);
            }
       },0,3000);
		return super.onStartCommand(intent, flags, startId);
	}

	@Override
	public void onDestroy() {
		// TODO Auto-generated method stub
		super.onDestroy();
		timer.cancel();
		Log.d("rock", "onDestroy");
	}
    private void sendNotice(){
        Intent nextIntent = new Intent(this, ThiefAlertActivity.class);
//        nextIntent.putExtra("var1", 123);


        // 用來產生一個 PendingIntent
//        TaskStackBuilder stackBuilder = TaskStackBuilder.create(this);
//        stackBuilder.addParentStack(ThiefAlertActivity.class);
//        stackBuilder.addNextIntent(nextIntent);
        PendingIntent pending =
                PendingIntent.getActivity(this,0,nextIntent,0);  
        
        // 準備建立一個 Notification 物件實體
        Notification.Builder builder = new Notification.Builder(this);
        builder.setSmallIcon(android.R.drawable.stat_sys_warning);
        builder.setTicker("有人侵入");
        builder.setLargeIcon(
                BitmapFactory.decodeResource(getResources(), R.drawable.stop));
        builder.setAutoCancel(true);
        builder.setContentInfo("Info");
        //builder.setContentText("Text:" + (int)(Math.random()*100));
        builder.setContentText("請確認是否為陌生人");
        builder.setContentTitle("有人侵入");
        builder.setWhen(System.currentTimeMillis());
        builder.setContentIntent(pending);
        Uri sound = Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.buzz);
        builder.setSound(sound);
        //builder.setSound(Uri.fromFile(new File(sdroot, "aircraft006.mp3")));


        int dot = 200;      // Length of a Morse Code "dot" in milliseconds
        int dash = 500;     // Length of a Morse Code "dash" in milliseconds
        int short_gap = 200;    // Length of Gap Between dots/dashes
        int medium_gap = 500;   // Length of Gap Between Letters
        int long_gap = 1000;    // Length of Gap Between Words
        long[] pattern = {
                0,  // Start immediately
                dot, short_gap, dot, short_gap, dot,    // s
                medium_gap,
                dash, short_gap, dash, short_gap, dash, // o
                medium_gap,
                dot, short_gap, dot, short_gap, dot,    // s
                long_gap
        };

        builder.setVibrate(pattern);


        // API Level 11+
//		Notification notification = builder.getNotification();
        // API Level 16+ (4.1.2+)
        Notification notification = builder.build();

        // 發出通知了
        mgr.notify(nid++, notification);

    }

}
