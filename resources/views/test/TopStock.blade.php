@extends('app')
@section('content')


    @if(count($gp)>0)
        <table class="table">
        <tr>
            <td>股票代码</td>
            <td>上市公司</td>
            <td>共同持有数</td>
        </tr>
    @foreach($gp as $per)
        <tr>
            <td>{{$per->gpcode}}</td>
            <td>{{$per->name}}</td>
            <td><a href="/details/{{$per->gpcode}}" target="_blank">{{$per->num}}</a></td>
        </tr>

    @endforeach
        </table>
    @endif

@endsection

@section('footer')
    {{ $gp->links() }}

@endsection