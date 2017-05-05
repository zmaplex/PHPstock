<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', 'ScodeController@orm1');

Route::get('/say',function(){
	return "hello world";
});

Route::get('/about','SiteController@about');
Route::get('/sql','SiteController@sql');
Route::get('/contact','SiteController@contact');
Route::get('/orm1','ScodeController@orm1');
Route::get('/TopStock','ScodeController@TopStock');
Route::get('/details', 'ScodeController@details');
Route::get('/details/{id}', 'ScodeController@details')->where('id','[0-9]+');