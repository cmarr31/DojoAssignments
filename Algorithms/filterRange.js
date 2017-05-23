function filterRange(a,min,max){
  console.log(a);
  console.log("min="+min);
  console.log("max="+max);
  var in_range=false;
  var temp;
  var i;
  while(in_range===false){
    for(i=0;i<a.length;i++){
      if(a[i]>min&&a[i]<max){
        in_range=true;
      }
      if(in_range===true&&a[i]<=min||a[i]>=max){
        //swap
        temp=a[i-1];
        a[i-1]=a[i];
        a[i]=temp;
        in_range=false;
      }
      else if(i==a.length&&a[i]>min&&a[i]<max){
        //swap
        temp=a[i-1];
        a[i-1]=a[i];
        a[i]=temp;
        in_range=false;
      }
    }
  }
  for(i=0;i<a.length;i++){
    if(a[i]>min&&a[i]<max){
      a.length=i;
    }
  }
  return a;
}
filterRange([0,1,2,3,3,4,5],2,4);