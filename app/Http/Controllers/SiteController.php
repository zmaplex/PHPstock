<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class SiteController extends Controller
{


    public function index()
    {
    	return view('welcome');
    }

    public function about()
    {	
        $people = ['a 1','b 2','c 3'];
    	return view('test.about',compact('people'));
    }

    public function contact()
    {
    	return view('test.contact');
    }

    public function sql()
    {
        $gp = DB::select('select * from scode');
        dd($gp);
    }


}
