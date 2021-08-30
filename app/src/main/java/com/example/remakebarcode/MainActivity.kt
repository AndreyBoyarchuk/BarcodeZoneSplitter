package com.example.remakebarcode

import android.R.attr
import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.zxing.integration.android.IntentIntegrator
import kotlinx.android.synthetic.main.activity_main.*
import android.R.attr.data

import android.widget.Toast
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

import com.google.zxing.integration.android.IntentResult




class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        btn_scan.setOnClickListener{
            val scanner=IntentIntegrator(this)
            scanner.setDesiredBarcodeFormats(IntentIntegrator.PDF_417)
            scanner.setBeepEnabled(false)
            scanner.initiateScan()
            if (! Python.isStarted()) {
                Python.start(AndroidPlatform(this))
            }
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        val result = IntentIntegrator.parseActivityResult(requestCode, resultCode, data)
        if (result != null) {
            if (result.contents == null) {
                Toast.makeText(this, "Cancelled", Toast.LENGTH_LONG).show()
            } else {
                var strOut:String=result.contents
                val python = Python.getInstance()
                val pythonFile= python.getModule("ForAndroid",)
                textView.text=pythonFile.callAttr("inputFirst",strOut).toString()
            }
        } else {
            super.onActivityResult(requestCode, resultCode, data)
        }
    }
}