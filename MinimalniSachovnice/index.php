<!DOCTYPE html><title>?</title><table><?php $t='<tr style="height:82px;">';$u='<td style="width:80px;"></td>';echo($t);for($i=0;$i<64;$i++){echo((strval($i/8%2)-$i%2?str_replace(';',';background-color:black;',$u):$u).(($i+1)%8==0?'</tr>'.($i!=63?$t:''):''));}?></table>