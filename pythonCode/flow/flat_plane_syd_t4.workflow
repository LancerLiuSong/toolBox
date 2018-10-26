<?xml version="1.0" encoding="utf-8"?>
<workflow version="1.0.0" id="ac3dd606-ea37-40a5-b0d8-1544ca0616a1" MemoryReqPerPoint="0">
	<plugin name="LAS Area Selector (Solar)" xposition="9.3333333333333712" yposition="171.16666666666657" id="f797be49-b88f-4288-8944-3f3ee8d1bb01">
		<setting name="Area Height" value="10000000"/>
		<setting name="Area Width" value="10000000"/>
		<setting name="Directory" value="D:\data\LIDAR\SydneyNorth0413\LAS\sub1"/>
		<setting name="Per Swathe Processing" value="false"/>
		<setting name="Spatial Reference" value="EPSG:28356 (MGA56)"/>
		<setting name="Tiles List" value=""/>
		<setting name="X Max" value="339784.69500000001"/>
		<setting name="X Min" value="339685.72399999999"/>
		<setting name="Y Max" value="6248707.7130000005"/>
		<setting name="Y Min" value="6248612.5549999997"/>
		<output name="Area List" value="Area In,9140009f-a8e8-40dd-8b10-3d09ba379502"/>
	</plugin>
	<plugin name="Area" xposition="272.66666666666663" yposition="157.49999999999994" id="9140009f-a8e8-40dd-8b10-3d09ba379502">
		<input name="Area In" value="Area List,f797be49-b88f-4288-8944-3f3ee8d1bb01"/>
		<output name="Area Out" value="Area,d41e23c1-c742-4520-b14e-cf9837e4301c"/>
	</plugin>
	<plugin name="Points (Solar)" xposition="535.33333333333337" yposition="161.5" id="d41e23c1-c742-4520-b14e-cf9837e4301c">
		<setting name="Add Context" value="false"/>
		<setting name="Data Option" value="Point Height,Scan Angle Rank,Intensity,Total Return Number,Return Number,Classification,Scan Direction Flag,Edge Of Flight Line,User Data,Point Source ID,Colour,GPS Time"/>
		<setting name="Include All Swathes" value="false"/>
		<setting name="Point Type" value="Never classified (0),Unassigned (1),Ground (2),Low Vegetation (3),Medium Vegetation (4),High Vegetation (5),Building (6),Model Key (8),Water (9),Bridge (10)"/>
		<setting name="Stop Workflow If Empty" value="true"/>
		<input name="Area" value="Area Out,9140009f-a8e8-40dd-8b10-3d09ba379502"/>
		<output name="Points Out" value="Points In,f4d29cd9-5cf3-4be9-9d64-a7e121c76bd2"/>
	</plugin>
	<plugin name="Flat Planes (Solar)" xposition="812.66666666666652" yposition="94.833333333333258" id="f4d29cd9-5cf3-4be9-9d64-a7e121c76bd2">
		<setting name="Output Raw Planes (Unfixed Shapes)" value="true"/>
		<setting name="Point Density" value="2"/>
		<output name="All Points Out" value=""/>
		<output name="Corrected Planes" value="Vector Shapes,fdce8e28-2a9f-403a-be6d-f3d2a2a4ef81"/>
		<input name="Points In" value="Points Out,d41e23c1-c742-4520-b14e-cf9837e4301c"/>
		<output name="Points Shape" value=""/>
		<output name="Raw Planes" value="Vector Shapes,a1910be9-53ae-4628-8548-c8979423466b"/>
	</plugin>
	<plugin name="Vector Shapes Export" xposition="1121.8333333333317" yposition="117.83333333333337" id="fdce8e28-2a9f-403a-be6d-f3d2a2a4ef81">
		<setting name="Directory" value="D:\data\LIDAR\SydneyNorth0413\LAS\sub1\out"/>
		<setting name="File Format" value="GeoJSON"/>
		<setting name="File Suffix" value="planesCrtT4"/>
		<setting name="Point Type" value="3D"/>
		<setting name="Spatial Reference" value="EPSG:4326 (WGS84)"/>
		<input name="Vector Shapes" value="Corrected Planes,f4d29cd9-5cf3-4be9-9d64-a7e121c76bd2"/>
	</plugin>
	<plugin name="Vector Shapes Export" xposition="1124.5" yposition="221.83333333333329" id="a1910be9-53ae-4628-8548-c8979423466b">
		<setting name="Directory" value="D:\data\LIDAR\SydneyNorth0413\LAS\sub1\out"/>
		<setting name="File Format" value="GeoJSON"/>
		<setting name="File Suffix" value="planesRawT4"/>
		<setting name="Point Type" value="3D"/>
		<setting name="Spatial Reference" value="EPSG:4326 (WGS84)"/>
		<input name="Vector Shapes" value="Raw Planes,f4d29cd9-5cf3-4be9-9d64-a7e121c76bd2"/>
	</plugin>
</workflow>
