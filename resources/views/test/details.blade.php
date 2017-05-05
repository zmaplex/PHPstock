@extends('app')
@section('content')
    @if(count($gp)>0)
    <h1>{{$gp[0]->gpcode}} - {{$gp[0]->name}}</h1>
    <table class="table">
        <tr>
            <td>基金公司</td>
            <td>基金代码 </td>
            <td>持仓比率</td>

        </tr>
    @foreach($gp as $per)
        <tr>
            <td><a href="http://fund.eastmoney.com/{{$per->jjcode}}.html" target="_blank">{{$per->jjname}}</a></td>
            <td>{{$per->jjcode}}</td>
            <td>{{$per->percent}}</td>
        </tr>
    @endforeach
    </table>
    {{ $gp->links() }}
    @else
        <p>抱歉,没找到相关页面</p>
    @endif

@stop