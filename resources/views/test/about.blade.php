@extends('app')

@section('content')
<h3>People i admire</h3>
@if (count($people)>0)
	{{-- expr --}}

<ul>
	@foreach($people as $person)
		<li>{{ $person }}</li>
	@endforeach
</ul>
@endif
@endsection