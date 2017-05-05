<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateScodeTable extends Migration
{
    /**
     * Run the migrations.
     *  code CHAR(10) NOT NULL PRIMARY KEY,
        name CHAR(60) NOT NULL,
        percent DOUBLE NOT NULL
     * @return void
     */
    public function up()
    {
        Schema::create('scode', function (Blueprint $table) {
            $table->increments('id');
            $table ->char('gpcode',10);
            $table ->char('name',60);
            $table ->double('percent',6,3);
            $table->char('jjcode',10);
            $table->char('jjname',100);
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        //
    }
}
