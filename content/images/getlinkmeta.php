<?php
/*
Plugin Name: Get Link Meta
Plugin URI: http://wordpress.org/extend/plugins/getlinkdescription
Description: Get Description from site-meta-data for links
Author: Elias Kirchgässner
Version: 0.1
License: GPL
Author URI: http://www.lioman.de
Update Server: http://wordpress.org/.. (Link zum Update-Server, wo das Plugin liegt.)
Min WP Version: 1.5
Max WP Version: 3.2.1

function getlinkmeta() {
if ($link->link_id != '')
	{
	$description= get_meta_tags($link_url);
	echo $description['description'];
	}
}
*/

global $wp_version;
if (version_compare($wp_version,"3.0","<")) /*provides the current WordPress version in standard format*/
{
 add_action('admin_init', 'addMetaBox', 1); /*for versions < 3.0*/
}
else
{
 add_action('add_meta_boxes', 'addMetaBox'); /*for versions >=3.0*/
}
 
function addMetaBox()
{
 add_meta_box( 'boxId', __( 'My Custom Box', 'myplugin_textdomain' ), 'renderHtml', 'post', 'normal', 'high', array('showname'=>true, 'showage'=>false, 'showaddress'=>true) );
}
 
function renderHtml($post, $params)
{
 $myParams = $params['args'];
 
 if($myParams['showname'])
 {
?>
 <label for="myname">Enter Your Name</label>
 
 <input type="text" name="myname" id="myname" />
 
 
<?php
 }
  
 if($myParams['showage'])
 {
?>
 <label for="myage">Enter Your Age</label>
 
 <input type="text" name="myage" id="myage" />
 
 
<?php
 }
 
 if($myParams['showaddress'])
 {
?>
 <label for="myaddress">Enter Your Address</label>
 
 <input type="text" name="myaddress" id="myaddress" />
<?php
 }
 
 // Use nonce for verification
 wp_nonce_field( plugin_basename(__FILE__), 'myNonce' );
}
?>
<?php
/* Do something with the data entered */
add_action('save_post', 'saveMyData');
 
function saveMyData( $post_id )
{
 // verify if this is an auto save routine. If it is our form has not been submitted, so we dont want to do anything
 if ( defined('DOING_AUTOSAVE') && DOING_AUTOSAVE ) 
  return $post_id;
 
 if ( !wp_verify_nonce( $_POST['myNonce'], plugin_basenamemyName = $_POST['myname'];
 $myAge = $_POST['myage'];
  

}
?>
