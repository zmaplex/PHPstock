@extends('app')
@section('content')
    <h1> 股票筛选 </h1>
    @if(count($gp)>0)
        <table class="table">
            <tr>
                <td data-toggle="tooltip" title="点击代码进入详情页面">股票代码</td>
                <td data-toggle="tooltip" title="点击公司名字查看财务报表">上市公司</td>
                <td>基金公司</td>
                <td>基金代码</td>
                <td>持仓比率</td>
            </tr>
            @foreach($gp as $per)
                <tr>
                    <td><a href="http://quote.eastmoney.com/{{$per -> gpcode}}.html" target="_blank">{{$per -> gpcode}}
                        </a></td>
                    <td><a href="http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code={{$per -> gpcode}}"
                           target="_blank">{{$per -> name}}</a></td>
                    <td>{{$per->jjname}}</td>
                    <td>{{$per -> jjcode}}</td>
                    <td>{{$per -> percent}}</td>


                </tr>
            @endforeach
        </table>
        {{ $gp->links() }}
    @endif

@endsection
