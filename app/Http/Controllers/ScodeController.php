<?php

namespace App\Http\Controllers;
use App\Scode;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class ScodeController extends Controller
{
    
    public function orm1()
    {

        $gp = DB::table('scode')->orderBy('gpcode','desc')->paginate(10);
        return view("test.stock",compact('gp'));
    }

    public function TopStock()
    {
        $gp = DB::table('scode')->select(DB::raw('gpcode,name ,COUNT(gpcode) as num'))->groupBy('gpcode','name')
            ->orderBy('num','desc')
            ->paginate(10);

        return view('test.TopStock',compact('gp'));
    }



    public function details($id='')
    {

        $gp = DB::table('scode')
            ->where('gpcode',$id)
            ->orderBy('jjcode','asc')
            ->paginate(10)
        ;
        return view('test.details',compact('gp'));
    }

}
