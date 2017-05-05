<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateJcodeTable extends Migration
{
  
    public function up()
    {
        Schema::create('jcode', function (Blueprint $table) {
            $table->increments('id');
            $table->char('jjcode',10)->unique();
            $table->string('name',100);
            $table->double('dwjz',15,3);
            $table->double('3ybdfd',15,3);
            $table->char('3ybdpj',10);
            $table->double('cxfxxx',10,3);
            $table->char('cxpj',10);
            $table->double('xpbl3y',6,3);
            $table->char('xppj3y',10);
            $table->double('fromyl',6,3);

            $table->timestamps();
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
