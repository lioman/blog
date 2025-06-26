Gravatar Hovercards einbinden
#############################
:date: 2010-10-12 13:26
:author: Lioman
:category: Digital
:tags: Blog, Gravatar, Hover, Javascript, Kommentare, script
:slug: gravatar-hovercards-einbinden
:status: published

-  **Update2: Einfacher geht es in Wordpress mit dem Plugin:** `Jetpack <http://jetpack.me/>`__
-  **Update: Der Minimierte Code geht noch nicht!!! Nur die ungepackte Version funktioniert!!!**

|image0| Schon länger ist der Dienst `Gravatar <http://www.gravatar.com>`__ 
in diversen Blogs eingebaut.
Sowohl bei wordpress.com als auch in vielen Privaten. Hat man also ein
Bild mit einer Emailadresse verknüpft erscheint es überall wo man
kommentiert (und der Dienst eingebunden ist). Seit einiger Zeit konnte
man ein Erweitertes Profil gestalten und ein klick auf das Bild neben
einem Kommentar führte zu diesem. Wenn man also möchte kann man so sein
Facebook-Profil - Twitterstream oder andere Konten bekannt machen und
verbreiten. Nun gibt es die Möglichkeit eben jene Informationen aus dem
Profil schon beim mit der Maus über das Bild gehen sich kompakt anzeigen
zu lassen.

Das Ergebnis sieht man oben im Bild und eingebaut ist es in ein Theme
mit wenigen Klicks.

So wird es eingebaut.
~~~~~~~~~~~~~~~~~~~~~

Einfach in die *functions.php* des Themes folgende Zeile einfügen:

.. code:: php

    wp_enqueue_script( 'gprofiles', 'http://s.gravatar.com/js/gprofiles.js', array( 'jquery' ), 'e', TRUE );

Möchte man das ganze noch mehr gestalten muss man sich ein kleines
Plugin schreiben. Eine genaue Anleitung dazu gibt es
`hier <http://blog.wordpress-deutschland.org/2010/10/10/gravatars-hovercard-verwenden.html>`__.
Daher habe ich auch die oben beschriebene Anleitung.

Verbessern
~~~~~~~~~~

In den Kommentaren hat `Thomas Scholz <http://toscho.de/>`__
geschrieben, dass das Skript erstens groß und zweitens mit einem
Wordpresstracker versehen ist. Möchte man das umgehen, kann man sich das
Skript herunterladen und bearbeiten. Ohne Tracker sieht es dann so aus
(Wenn ich alles erwischt habe):

.. code:: js

   if ( \undefined\ == typeof( console ) ) {
    console = { \log\: function(str){}, \debug\: function(str){} };
   }

   var Gravatar = {
    /* All loaded profiles, keyed off ghash */
    \profile_stack\: {},

    // Mapping of ghash to the \currently waiting\ dom_id of where to render it
    \profile_map\: {},

    /* Timeouts for hovering over and off Gravatar images */
    \overTimeout\: false,
    \outTimeout\: false,

    /* If true, show_card will bail */
    \stopOver\: false,

    /* The img element, hash and ID of the Gravatar that is being hovered over */
    \active_grav\: false,
    \active_hash\: false,
    \active_id\: false,

    /* The clone of the Gravatar img element that is being hovered over. */
    \active_grav_clone\: false,

    /* Callback function for once a profile is loaded */
    \profile_cb\: null,

    /* Wating throbber */
    \throbber\: null,

    /* Has a custom background image been added to the card? */
    \has_bg\: false,
    \disabled\:false,

    \mouseOut\: function(e) {
    e.stopImmediatePropagation();
    Gravatar.stopOver = true;

    // console.debug( ':set out' );
    Gravatar.outTimeout = setTimeout( function() {
    // console.debug( ':do out' );
    Gravatar.hide_card();
    }, 300 );
    },

    \init\: function() {
    var ca = document.cookie.split( ';' ), i, c;
    for ( i = 0; i &lt; ca.length; i++ ) {
    c = ca[i];
    while ( ' ' == c.charAt(0) ) {
    c=c.substring( 1, c.length );
    }
    if ( 0 == c.indexOf( 'nohovercard=1' ) ) {
    return;
    }
    }

    /* Locate all Gravatar images and attach profile links to them. */
    this.attach_profiles();

    /* Add CSS */
    this.add_card_css();

    /* Find and show a hovercard when hovering over a Gravatar. */
    jQuery('img.grav-hashed').live( 'mouseenter.gravatar mouseleave.gravatar', function(e) {
    if ( Gravatar.disabled ) { return; }
    e.preventDefault();
    e.stopPropagation();

    if ( 'mouseleave' == e.type || 'mouseout' == e.type ) {
    // console.debug( 'grav out' );
    return Gravatar.mouseOut.call( this, e );
    }

    Gravatar.stopOver = false;

    // console.debug( 'grav enter' );
    /* Get and store the hash and ID for the active Gravatar */
    Gravatar.active_id = jQuery(this).attr('id');
    Gravatar.active_hash = Gravatar.active_id.split('-')[1];

    Gravatar.untilt_gravatar();

    // console.debug( ':clear over1' );
    clearTimeout( Gravatar.overTimeout );

    // No profile data - see fetch_profile_error
    if ( false === Gravatar.profile_map[ 'g' + Gravatar.active_hash ] ) {
    return;
    }

    // console.debug( ':clear out' );
    clearTimeout( Gravatar.outTimeout );

    Gravatar.tilt_gravatar();
    Gravatar.fetch_profile_by_hash( Gravatar.active_hash, Gravatar.active_id );
    // console.debug( ':set over' );
    Gravatar.overTimeout = setTimeout( function() {
    Gravatar.show_card();
    }, 600 );
    });

    /* Maintain hovercard state when rolling over a hovercard or cloned image */
    jQuery('div.gcard, img.grav-clone').live( 'mouseenter.gravatar mouseleave.gravatar', function(e) {
    if ( Gravatar.disabled ) { return; }
    e.preventDefault();
    e.stopPropagation();

    if ( e.type == 'mouseenter' || e.type == 'mouseover' ) {
    Gravatar.stopOver = false;

    // console.debug( 'clone enter' );
    // console.debug( ':clear out2' );
    clearTimeout( Gravatar.outTimeout );
    } else {
    // console.debug( 'clone out' );
    Gravatar.mouseOut.call( this, e );
    }
    });

    /* Cancel a hovercard when scrolling. */
    jQuery(window).bind( 'scroll', function() {
    if ( !Gravatar.active_hash.length )
    return;

    Gravatar.hide_card();
    });
    },

    \attach_profiles\: function( container ) {
    /* Locate all Gravatar images and add profiles to them */
    container = \undefined\ == typeof( container ) ? \body\ : container;

    jQuery( container + ' img[src*=gravatar.com/avatar]' ).not( '.no-grav, .no-grav img' ).each( function() {
    hash = Gravatar.extract_hash( this );

    /* Add unique ID to image so we can reference it directly */
    uniq = 0;
    if ( jQuery( '#grav-' + hash + '-' + uniq ).length ) {
    while ( jQuery( '#grav-' + hash + '-' + uniq ).length )
    uniq++;
    }

    /* Remove the hover titles for sanity */
    var g = jQuery( this ).attr( 'id', 'grav-' + hash + '-' + uniq ).attr( 'title', '' ).removeAttr( 'title' );
    if ( g.parent( 'a' ).length )
    g.parent( 'a' ).attr( 'href', 'http://gravatar.com/' + hash ).attr( 'title', '' ).removeAttr( 'title' );

    g.addClass('grav-hashed');
    });
    },

    \show_card\: function() {
    if ( Gravatar.stopOver ) {
    return;
    }

    dom_id = this.profile_map[ 'g' + Gravatar.active_hash ];

    // Close any existing cards
    jQuery( '.gcard' ).hide();

    // Bail if we're waiting on a fetch
    if ( 'fetching' == this.profile_stack[ 'g' + Gravatar.active_hash ] ) {
    Gravatar.show_throbber();
    this.listen( Gravatar.active_hash, 'show_card' );
    // console.log( 'still fetching ' + hash );
    return;
    }

    // If we haven't fetched this profile yet, do it now and do this later
    if ( 'undefined' == typeof( this.profile_stack[ 'g' + Gravatar.active_hash ] ) ) {
    Gravatar.show_throbber();
    this.listen( Gravatar.active_hash, 'show_card' );
    // console.log( 'need to start fetching ' + hash + '@' + dom_id );
    this.fetch_profile_by_hash( Gravatar.active_hash, dom_id );
    return;
    }

    Gravatar.hide_throbber();

    // console.log( 'show_card: hash: ' + hash + ', DOM ID: ' + dom_id );

    // No HTML? build it
    if ( !jQuery( '#profile-' + this.active_hash  ).length )
    this.build_card( this.active_hash, this.profile_stack[ 'g' + this.active_hash ] );

    this.render_card( this.active_grav, 'profile-' + this.active_hash );
    },

    \hide_card\: function() {
    // console.debug( ':clear over3' );
    clearTimeout( Gravatar.overTimeout );

    /* Untilt the Gravatar image */
    this.untilt_gravatar();
    grav_resize.current_image = false
    jQuery( 'div.gcard' ).filter( '#profile-' + this.active_hash ).fadeOut(120, function() {
    jQuery('img.grav-large').stop().remove();
    } ).end().not( '#profile-' + this.active_hash ).hide();
    },

    \render_card\: function( grav, card_id ) {
    var card_el = jQuery( '#' + card_id  ).stop();

    // console.log( 'render_card for ' + grav_id + ', ' + card_id );
    // Change CSS positioning based on where grav_id is in the page
    var grav_el  = grav;
    var grav_pos = grav_el.offset();

    if ( null != grav_pos ) {
    var grav_width  = grav_el.width();
    var grav_height = grav_el.height();
    var grav_space  = 5 + ( grav_width * .4 );

    var card_width  = card_el.width();
    var card_height = card_el.height();
    if ( card_width == jQuery(window).width() ) {
    card_width  = 400;
    card_height = 200;
    }

    /*
    console.log( grav_pos );
    console.log( 'grav_width = ' + grav_width + \\n\ +
    'grav_height = ' + grav_height + \\n\ +
    'grav_space = ' + grav_space + \\n\ +
    'card_width = ' + card_width + \\n\ +
    'card_height = ' + card_height + \\n\ );
    */

    /* Position to the right of the element */
    var left = grav_pos.left + grav_width + grav_space;
    var top = grav_pos.top;
    var grav_pos_class = 'pos-right';

    /* Position to the left of the element if space on the right is not enough. */
    if ( grav_pos.left + grav_width + grav_space + card_width &gt; jQuery(window).width() + jQuery(window).scrollLeft() ) {
    left = grav_pos.left - ( card_width + grav_space );
    grav_pos_class = 'pos-left';
    }

    /* Reposition the card itself */
    var top_offset = grav_height * .25;
    jQuery( '#' + card_id ).removeClass( 'pos-right pos-left' ).addClass( grav_pos_class ).css( { 'top': ( top - top_offset ) + 'px', 'left': left + 'px' } );

    /* Position of the small arrow in relation to the Gravatar */
    var arrow_offset = ( grav_height / 2 );
    if ( arrow_offset &gt; card_height )
    arrow_offset = card_height / 2;
    if ( arrow_offset &gt; ( card_height / 2 ) - 6 )
    arrow_offset = ( card_height / 2 ) - 6;
    if ( arrow_offset &gt; 53 )
    arrow_offset = 53; // Max
    if ( this.has_bg )
    arrow_offset = arrow_offset - 8;
    if ( arrow_offset &lt; 0 )
    arrow_offset = 0; // Min
    var css = {
    'height': ( ( grav_height * 1.5 ) + top_offset ) + 'px'
    };
    if ( 'pos-right' == grav_pos_class ) {
    css['right'] = 'auto';
    css['left'] = '-7px';
    css['background-position'] = '0px ' + arrow_offset + 'px';
    } else {
    css['right'] = '-10px';
    css['left'] = 'auto';
    css['background-position'] = '0px ' + arrow_offset + 'px';
    }
    jQuery( '#' + card_id + ' .grav-cardarrow' ).css( css );
    }

    card_el.stop().css( { opacity: 0 } ).show().animate( { opacity: 1 }, 150, 'linear', function() {
    jQuery( this ).stop();
    grav_resize.init( card_id );
    grav_gallery.init( card_id );
    });
    },

    \build_card\: function( hash, profile ) {
    Object.size = function(obj) {
    var size = 0, key;
    for (key in obj) {
    if (obj.hasOwnProperty(key)) size++;
    }
    return size;
    };

    // console.log( 'Build profile card for: ' + hash );
    // console.log( profile );
    GProfile.init( profile );

    urls = GProfile.get( 'urls' );
    photos = GProfile.get( 'photos' );
    services = GProfile.get( 'accounts' );

    limit = 100;
    if ( Object.size( urls ) &gt; 3 )
    limit += 90;
    else
    limit += 10 + ( 20 * Object.size( urls ) );

    if ( Object.size( services ) &gt; 0 )
    limit += 30;

    description = GProfile.get( 'aboutMe' );
    description = description.replace( /&lt;[^&gt;]+&gt;/ig, '' );
    description = description.toString().substr( 0, limit );
    if ( limit == description.length )
    description += '<span class="removed_link" title="\'">&amp;#8230;</span>';

    var card_class = 'grav-inner';

    // console.log( Gravatar.my_hash, hash );
    if ( Gravatar.my_hash &amp;&amp; hash == Gravatar.my_hash ) {
    card_class += ' grav-is-user';
    if ( !description.length ) {
    description = \</pre>
   Want a better profile? <a class="grav-edit-profile" href="http://gravatar.com/profiles/edit/" target="_blank">Click here</a>.
   <pre lang="js">\;
    }
    }

    if ( description.length ) {
    card_class += ' gcard-about';
    }

    card = '</pre>
   <div id="\profile-'">

   \
   <div>

   \
   <div>

   \
   <h4><span class="removed_link" title="\'">' + GProfile.get( 'displayName' ) + '</span></h4>
   \\ ' + description + ' \

   \

   </div>
   \
   <div>

   '; if ( Object.size( urls ) || Object.size( services ) ) { card_class += ' gcard-links'; } card += '
   <h5>Personal Links</h5>
   \
   <ul>
   <ul>'; url_count = 0; for ( var u in urls ) { if ( !urls[u]['value'] || !urls[u]['title'] ) continue; if ( url_count &gt; 2 ) { card += '
       <li><span class="removed_link" title="\'"> + ' + ( urls.length - url_count )  + ' more</span></li>
   </ul>
   </ul>
   '; break; } card += '
   <ul>
   <ul>
       <li><span class="removed_link" title="\'">' + urls[u]['title'] + '</span></li>
   </ul>
   </ul>
   '; url_count++; } card += '

   '; // console.log( 'Services to include in card:' ); // console.log( services ); if ( Object.size( services ) ) { card_class += ' gcard-services'; } card += '
   <ul>
   <ul>'; services_out = 0; for ( var s in services ) { if ( !services[s]['url'] ) continue; if ( services_out &gt;= 6 ) break; card += '
       <li></li>
   </ul>
   </ul>
   '; services_out++; } card += '

   '; card += '

   </div>
   '; // right col if ( Object.size( photos ) &gt; 1 ) { card_class += ' gcard-gallery'; } card += '
   <div>

   \ Previous \
   <div>

   \
   <ul>
   <ul>'; for ( var p in photos ) { if ( !photos[p]['value'] ) continue; card += '
       <li></li>
   </ul>
   </ul>
   '; } card += '

   \

   </div>
   \ Next \

   </div>
   '; // gallery card += '
   <div></div>
   \
   <div><a title="\Powered" href="\http://gravatar.com/\" target="\_blank\">&amp;nbsp;</a></div>
   \
   <div style="\clear: both\;;"></div>
   '; card += 'Turn off hovercards

   '; card += '

   </div>
   </div>
   <pre lang="js">'; // .grav-inner, .gcard

    // console.log( 'Finished building card for ' + dom_id );
    jQuery( 'body' ).append( jQuery( card ) );
    jQuery( '#profile-' + hash + ' .grav-inner' ).addClass( card_class );

    // Custom Background
    this.has_bg = false;
    bg = GProfile.get( 'profileBackground' );
    if ( Object.size( bg ) ) {
    this.has_bg = true;
    var bg_css = {
    padding: '8px 0'
    };
    if ( bg.color )
    bg_css['background-color'] = bg.color;
    if ( bg.url )
    bg_css['background-image'] = 'url(' + bg.url + ')';
    if ( bg.position )
    bg_css['background-position'] = bg.position;
    if ( bg.repeat )
    bg_css['background-repeat'] = bg.repeat;
    jQuery( '#profile-' + hash ).css( bg_css );
    }

    // Resize card based on what's visible
    if ( !jQuery( '#profile-' + hash + ' .gcard-links' ).length &amp;&amp; !jQuery( '#profile-' + hash + ' .gcard-services' ).length )
    jQuery( '#profile-' + hash + ' .grav-rightcol' ).css( { 'width': 'auto' } );
    if ( !jQuery( '#profile-' + hash + ' .gcard-about' ).length )
    jQuery( '#profile-' + hash + ' .grav-leftcol' ).css( { 'width': 'auto' } );

    // Trigger callback if defined
    if ( jQuery.isFunction( Gravatar.profile_cb ) ) {
    Gravatar.loaded_js( hash, 'profile-' + hash );
    }

    },

    \tilt_gravatar\: function() {
    /* Set the active gravatar */
    this.active_grav = jQuery('img#' + this.active_id);

    if ( jQuery('img#grav-clone-' + this.active_hash).length )
    return;

    /* Clone the image */
    this.active_grav_clone = this.active_grav.clone().attr( 'id', 'grav-clone-' + this.active_hash ).addClass('grav-clone');

    var top = this.active_grav.offset().top;
    var left = this.active_grav.offset().left;
   /*
    top  -= 2;
    left -= 2;
   */

    /* Style clone */
    var fancyCSS = {
    '-webkit-transform': 'rotate(-4deg) scale(1.3)',
    '-moz-transform': 'rotate(-4deg) scale(1.3)',
    '-o-transform': 'rotate(-4deg) scale(1.3)',
    'transform': 'rotate(-4deg) scale(1.3)',
    '-webkit-box-shadow': '0 0 4px #aaa',
    '-moz-box-shadow': '0 0 4px #aaa',
    'box-shadow': '0 0 4px #aaa',
    'border-width': '2px 2px ' + ( this.active_grav.height() / 5 ) + 'px 2px',
    'border-color': '#fff',
    'border-style': 'solid',
    'padding': '0px'
    };
    if ( jQuery.browser.msie &amp;&amp; 9 &gt; jQuery.browser.version ) {
    fancyCSS['filter'] = \progid:DXImageTransform.Microsoft.Matrix(M11='1.29683327', M12='0.0906834159', M21='-0.0906834159', M22='1.29683327', SizingMethod='auto expand') progid:DXImageTransform.Microsoft.Glow(Color='#aaaaaa', strength='2'\;
    top  -= 5;
    left -= 6;
    }
    var appendix = this.active_grav_clone.css( fancyCSS ).wrap( '' ).parent().css( {
    'position': 'absolute',
    'top': top + 'px',
    'left': left + 'px',
    'z-index': 15,
    'border': 'none',
    'text-decoration': 'none'
    } );

    /* Append the clone on top of the original */
    jQuery('body').append( appendix );
    this.active_grav_clone.removeClass('grav-hashed');
    },

    \untilt_gravatar\: function() {
    jQuery('img.grav-clone, a.grav-clone-a').remove();
    Gravatar.hide_throbber();
    },

    \show_throbber\: function() {
    // console.log( 'throbbing...' );
    if ( !Gravatar.throbber ) {
    Gravatar.throbber = jQuery( '</pre>
   <div id="\grav-throbber\"><img src="\http://s.gravatar.com/images/throbber.gif\" alt="\.\" width="\15\" height="\15\" /></div>
   <pre lang="js">' );
    }

    jQuery( 'body' ).append( Gravatar.throbber );

    var offset = jQuery('#' + Gravatar.active_id).offset();

    Gravatar.throbber.css( {
    top: offset.top + 2 + 'px',
    left: offset.left + 1 + 'px'
    } );
    },

    \hide_throbber\: function() {
    // Remove the throbber if it exists.
    if ( !Gravatar.throbber ) {
    return;
    }
    // console.log( 'stopped throbbing.' );
    Gravatar.throbber.remove();
    },

    /***
    * Helper Methods
    */

    \fetch_profile_by_email\: function( email ) {
    // console.debug( 'fetch_profile_by_email' );
    return this.fetch_profile_by_hash( this.md5( email ) );
    },

    \fetch_profile_by_hash\: function( hash, dom_id ) {
    // This is so that we know which specific Grav is waiting on us
    this.profile_map[ 'g' + hash ] = dom_id;
    // console.log( this.profile_map );

    // If we already have it, no point getting it again, so just return it and notify any listeners
    if ( this.profile_stack[ 'g' + hash ] &amp;&amp; 'object' == typeof( this.profile_stack[ 'g' + hash ] ) )
    return this.profile_stack[ 'g' + hash ];

    // console.log( 'fetch_profile_by_hash: ' + hash, dom_id );
    this.profile_stack[ 'g' + hash ] = 'fetching';
    // Not using $.getJSON because it won't call an error handler for remote URLs
    this.load_js( 'http://en.gravatar.com/' + hash + '.json?callback=Gravatar.fetch_profile_callback', function() {
    Gravatar.fetch_profile_error( hash, dom_id );
    } );
    },

    \fetch_profile_callback\: function( profile ) {
    if ( !profile || 'object' != typeof( profile ) )
    return;
    // console.log( 'Received profile via callback:' );
    // console.log( profile );
    this.profile_stack[ 'g' + profile.entry[0].hash ] = profile;
    this.notify( profile.entry[0].hash );
    },

    \fetch_profile_error\: function( hash, dom_id ) {
    Gravatar.profile_map[ 'g' + hash ] = false;
    var grav = jQuery( '#' + dom_id );
    if ( grav.parent( 'a[href=http://gravatar.com/' + hash + ']' ).size() ) {
    grav.unwrap();
    }
    // console.debug( dom_id, Gravatar.active_id );
    if ( dom_id == Gravatar.active_id ) {
    Gravatar.hide_card();
    }
    },

    \listen\: function( key, callback ) {
    if ( !this.notify_stack )
    this.notify_stack = {};

    key = 'g' + key; // Force valid first char
    // console.log( 'listening for: ' + key );
    if ( !this.notify_stack[ key ] )
    this.notify_stack[ key ] = [];

    // Make sure it's not already queued
    for ( a = 0; a &lt; this.notify_stack[ key ].length; a++ ) {
    if ( callback == this.notify_stack[ key ][ a ] ) {
    // console.log( 'already' );
    return;
    }
    }

    this.notify_stack[ key ][ this.notify_stack[ key ].length ] = callback;
    // console.log( 'added listener: ' + key + ' =&gt; ' + callback );
    // console.log( this.notify_stack );
    },

    \notify\: function( key ) {
    // console.log( 'trigger notification: ' + key );
    if ( !this.notify_stack )
    this.notify_stack = {};

    key = 'g' + key; // Force valid first char
    if ( !this.notify_stack[ key ] )
    this.notify_stack[ key ] = [];

    // Reverse it so that notifications are sent in the order they were queued
    // console.log( 'notifying key: ' + key + ' (with ' + this.notify_stack[ key ].length + ' listeners)' );
    for ( a = 0; a &lt; this.notify_stack[ key ].length; a++ ) {
    if ( false == this.notify_stack[ key ][ a ] || \undefined\ == typeof( this.notify_stack[ key ][ a ] ) )
    continue;

    // console.log( 'send notification to: ' + this.notify_stack[ key ][ a ] );
    Gravatar[ this.notify_stack[ key ][ a ] ]( key.substr( 1 ) );
    this.notify_stack[ key ][ a ] = false;
    }
    },

    \extract_hash\: function( str ) {
    // Get hash from img src
    hash = /gravatar.com\/avatar\/([0-9a-f]{32})/.exec( jQuery( str ).attr( 'src' ) );
    if ( null != hash &amp;&amp; \object\ == typeof( hash ) &amp;&amp; 2 == hash.length ) {
    hash = hash[1];
    } else {
    hash = /gravatar_id\=([0-9a-f]{32})/.exec( jQuery( str ).attr( 'src' ) );
    if ( null !== hash &amp;&amp; \object\ == typeof( hash ) &amp;&amp; 2 == hash.length ) {
    hash = hash[1];
    } else {
    return false;
    }
    }
    return hash;
    },

    \load_js\: function( src, error_handler ) {
    if ( !this.loaded_scripts )
    this.loaded_scripts = [];

    if ( this.loaded_scripts[ src ] )
    return;

    this.loaded_scripts[ src ] = true;

    var new_script = document.createElement( 'script' );
    new_script.src = src;
    new_script.type = 'text/javascript';
    if ( jQuery.isFunction( error_handler ) ) {
    new_script.onerror = error_handler;
    }

    // console.log( src );
    document.getElementsByTagName( 'head' )[0].appendChild( new_script );
    },

    \loaded_js\: function( hash, dom_id ) {
    Gravatar.profile_cb( hash, dom_id );
    },

    \add_card_css\: function() {
    if ( jQuery( '#gravatar-card-css' ).length )
    return;

    var urlS = jQuery( 'script[src*=gravatar.com/js/gprofiles.js]' ), url;
    if ( urlS.size() )
    url = urlS.attr( 'src' ).replace( /\/js\/gprofiles\.js.*$/, '' );
    else
    url = 'http://s.gravatar.com';

    new_css = \\;
    new_css += \\;

    jQuery( 'head' ).append( new_css );
    // console.log( 'Added CSS for profile cards to DOM' );
    },

    \md5\: function( str ) {
    return hex_md5( str );
    },

    \autofill\: function( email, map ) {
    // console.log('autofill');
    if ( !email.length || -1 == email.indexOf( '@' ) )
    return;

    this.autofill_map = map;
    hash = this.md5( email );
    // console.log( this.profile_stack[ 'g' + hash ] );
    if ( \undefined\ == typeof( this.profile_stack[ 'g' + hash ] ) ) {
    this.listen( hash, 'autofill_data' );
    this.fetch_profile_by_hash( hash );
    } else {
    // console.log( 'stack: ' + this.profile_stack[ 'g' + hash ] );
    this.autofill_data( hash );
    }
    },

    \autofill_data\: function( hash ) {
    // console.log( this.autofill_map );
    // console.log( this.profile_stack[ 'g' + hash ] );
    GProfile.init( this.profile_stack[ 'g' + hash ] );
    for ( var m in this.autofill_map ) {
    // console.log( m );
    // console.log( this.autofill_map[ m ] );
    switch ( m ) {
    case 'url':
    link = GProfile.get( 'urls' );
    // console.log( link );
    jQuery( '#' + this.autofill_map[ m ] ).val( link[0][ 'value' ] );
    break;
    case 'urls':
    links = GProfile.get( 'urls' );
    links_str = '';
    // console.log( links );
    for ( l = 0; l &lt; links.length; l++ ) {
    links_str += links[ l ][ 'value' ] + \\n\;
    }
    jQuery( '#' + this.autofill_map[ m ] ).val( links_str );
    break;
    default:
    parts = m.split( /\./ );
    if ( parts[ 1 ] ) {
    val = GProfile.get( m );
    switch ( parts[ 0 ] ) {
    case 'ims':
    case 'phoneNumbers':
    val = val.value;
    break;
    case 'emails':
    val = val[0].value;
    case 'accounts':
    val = val.url;
    break;
    }
    jQuery( '#' + this.autofill_map[ m ] ).val( val );
    } else {
    jQuery( '#' + this.autofill_map[ m ] ).val( GProfile.get( m ) );
    }
    }
    }
    },

    \whee\: function() {
    if ( Gravatar.whee.didWhee ) {
    return;
    }
    Gravatar.whee.didWhee = true;
    if ( document.styleSheets[0].addRule ) {
    document.styleSheets[0].addRule( '.grav-tag a', 'background-position: 22px 100% !important' );
    } else {
    jQuery( '.grav-tag a' ).css( 'background-position', '22px 100%' );
    }
    jQuery( 'img[src*=gravatar.com/]' ).addClass( 'grav-whee' ).css( {
    '-webkit-box-shadow': '1px 1px 3px #aaa',
    '-moz-box-shadow': '1px 1px 3px #aaa',
    'box-shadow': '1px 1px 3px #aaa',
    'border': '2px white solid'
    } );
    var i = 0;
    setInterval( function() {
    jQuery( '.grav-whee' ).css( {
    '-webkit-transform': 'rotate(-' + i + 'deg) scale(1.3)',
    '-moz-transform': 'rotate(-' + i + 'deg) scale(1.3)',
    'transform': 'rotate(-' + i + 'deg) scale(1.3)'
    });
    i++;
    if ( 360 == i ) {
    i = 0;
    }
    }, 6 );
    return false;
    },

   }

   jQuery( function() {
    Gravatar.init();
   });

   /**
    * Provides an interface for acceseing profile data returned from Gravatar.com.
    * Use GProfile.init() to set up data, based on the JSON returned from Gravatar,
    * then GProfile.get() to access data more easily.
    */
   var GProfile = {
    \data\: {},

    \init\: function( data ) {
    if ( 'fetching' == data )
    return false;
    if ( 'undefined' == typeof( data.entry[0] ) )
    return false;
    GProfile.data = data.entry[0];
    },

    /**
    * Returns a value from the profile data.
    * @param string attr The name of the attribute you want
    * @param int num (Optional) 0-based array index of the value from this attribute. Use 0 if you're not sure
    * @return Mixed value of the attribute, or empty string.
    */
    \get\: function( attr ) {
    // Handle x.y references
    if ( -1 != attr.indexOf( '.' ) ) {
    parts = attr.split( /\./ );
    // console.log(parts);
    if ( GProfile.data[ parts[ 0 ] ] ) {
    if ( GProfile.data[ parts[ 0 ] ][ parts[ 1 ] ] )
    return GProfile.data[ parts[ 0 ] ][ parts[ 1 ] ]

    for ( i = 0, s = GProfile.data[ parts[ 0 ] ].length; i &lt; s; i++ ) {
    if ( GProfile.data[ parts[ 0 ] ][ i ].type &amp;&amp; parts[ 1 ] == GProfile.data[ parts[ 0 ] ][ i ].type // phoneNumbers | ims
    || GProfile.data[ parts[ 0 ] ][ i ].shortname &amp;&amp; parts[ 1 ] == GProfile.data[ parts[ 0 ] ][ i ].shortname // accounts
    || GProfile.data[ parts[ 0 ] ][ i ].primary &amp;&amp; parts[ 1 ] == 'primary' ) { // emails

    return GProfile.data[ parts[ 0 ] ][ i ];
    }
    }
    }

    return '';
    }

    // Handle \top-level\ elements
    if ( GProfile.data[ attr ] )
    return GProfile.data[ attr ];

    // And some \aliases\
    if ( 'url' == attr ) {
    if ( GProfile.data.urls.length )
    return GProfile.data.urls[0].value;
    }

    return '';
    }
   };

   var grav_resize = {
    card_id: '',
    orig_width: 0,
    orig_height: 0,
    orig_top: 0,
    orig_left: 0,
    current_image: false,

    init: function( card_id ) {
    grav_resize.card_id = card_id;
    grav_resize.bind_enlarge();
    },

    enlarge: function( el ) {
    /* Remove any enlarged images */
    if ( jQuery('img.grav-large').stop().remove().size() ) {
    grav_resize.current_image = false;
    return;
    }

    grav_resize.current_image = el.attr( 'src' );
    /* Preload the larger version of the image */
    jQuery( '#' + grav_resize.card_id + ' .grav-tag a' ).css( 'background-position', '22px 100%' );
    var fullsize = jQuery('<img alt="" />').attr( 'src', grav_resize.current_image + '&amp;size=400' ).load( function() {
    jQuery( '#' + grav_resize.card_id + ' .grav-tag a' ).css( 'background-position', '22px 0' );
    } );

    /* Clone the image */
    var the_clone = el.clone();

    the_clone.css({
    'position': 'absolute',
    'top': grav_resize.orig_top,
    'left': grav_resize.orig_left,
    'background-color': '#333',
    'width': grav_resize.orig_width,
    'height': grav_resize.orig_height,
    'border-color': '#555'
    });

    the_clone.appendTo(el.parent());

    /* Get the image ratio */
    var    horiz_padding = 0;
    var    vert_padding = 0;
    var border_width = 6;
    var card = jQuery( '#' + grav_resize.card_id + ' .grav-inner' );

    if ( el.width() &gt; el.height() ) {
    var ratio = el.height() / el.width();
    var width = card.outerWidth();
    var height = ( width * ratio );
    var vert_padding = ( card.outerHeight() - height ) / 2;

    // if height it too big resize it width wise.
    if ( height &gt; card.outerHeight() ) {
    var ratio = el.width() / el.height();
    var height = card.outerHeight();
    var width = ( height * ratio );
    var horiz_padding = ( card.outerWidth() - width ) / 2;
    }

    } else {
    var ratio = el.width() / el.height();
    var height = card.outerHeight();
    var width = ( height * ratio );
    var horiz_padding = ( card.outerWidth() - width ) / 2;
    }

    the_clone.stop().animate({
    'top': 0,
    'left': 0,
    'width': width - border_width + 'px',
    'height': height - border_width + 'px',
    'z-index': 99,
    'padding-left': horiz_padding + 'px',
    'padding-right': horiz_padding + 'px',
    'padding-top': vert_padding + 'px',
    'padding-bottom': vert_padding + 'px'
    }, 250, function() {
    /* Make the clone the fullsize image that was preloaded */
    the_clone.addClass('grav-large');
    the_clone.attr('src', fullsize.attr('src') );

    /* Add the close button */
    the_clone.parent().append('</pre>
   <div>X</div>
   <pre lang="js">');
    jQuery('.grav-large-close').hide().fadeIn(100);
    } );

    jQuery('#'+grav_resize.card_id+' .grav-gallery img').unbind('click');

    jQuery('.grav-large-close' ).live( 'click', function() {
    grav_resize.reduce( the_clone );
    });

    jQuery(the_clone).click( function() {
    grav_resize.reduce( the_clone );
    });
    },

    reduce: function( el ) {
    jQuery('.grav-large-close').remove();

    el.stop().animate({
    'top': grav_resize.orig_top,
    'left': grav_resize.orig_left,
    'width': grav_resize.orig_width,
    'height': grav_resize.orig_height,
    'padding-left': 0,
    'padding-right': 0,
    'padding-top': 0,
    'padding-bottom': 0
    }, 250, function() {
    jQuery('img.grav-large').remove();
    grav_resize.bind_enlarge( grav_resize.card_id );
    grav_resize.current_image = false;
    });
    },

    bind_enlarge: function() {
    jQuery('#' + grav_resize.card_id + ' .grav-gallery img').parent( 'a' ).click( function(e) {
    if ( jQuery.browser.msie &amp;&amp; jQuery.browser.version &lt; 9.0 )
    return;

    e.preventDefault();

    if ( grav_resize.current_image ) {
    return;
    }

    var img = jQuery(this).find( 'img' ).not( '.grav-large' );
    var position = img.position();

    grav_resize.orig_width = img.width();
    grav_resize.orig_height = img.height();
    grav_resize.orig_top = position.top;
    grav_resize.orig_left = position.left;

    grav_resize.enlarge( img );
    });
    }
   }

   var grav_gallery = {
    orig_left: 0,
    pos: 0,

    init: function( card ) {
    grav_gallery.bind_arrows( card, true );

    /* Also recheck the arrows are correct once the user hovers over the gallery section, in case the images took a while to load */
    jQuery('#' + card + ' .grav-gallery').mouseover( function() {
    grav_gallery.bind_arrows( card, false );
    });
    },

    bind_arrows: function( card, reset ) {
    var gallery_el = jQuery('#' + card + ' .grav-gallery ul');
    if ( !gallery_el.size() ) {
    return;
    }
    grav_gallery.orig_left = gallery_el.css('margin-left').replace('px','');
    grav_gallery.pos = gallery_el.find( 'li:last').position();

    jQuery('#' + card + ' a.grav-gallery-next').live( 'click', function() {
    if ( grav_gallery.pos.left &gt; 275 )
    gallery_el.animate({'margin-left': parseFloat(grav_gallery.orig_left) - 314 + 'px'}, 300, function() { grav_gallery.highlight_arrows( card, false ); } );

    return false;
    });

    jQuery('#' + card + ' a.grav-gallery-prev').live( 'click', function() {
    if ( 0 != grav_gallery.orig_left )
    gallery_el.animate({'margin-left': parseFloat(grav_gallery.orig_left) + 314 + 'px'}, 300, function() { grav_gallery.highlight_arrows( card, false ) } );

    return false;
    });

    if ( reset )
    jQuery('#' + card + ' .grav-gallery ul').css({'margin-left': 0});

    grav_gallery.highlight_arrows( card, true );
    },

    highlight_arrows: function( card ) {
    grav_gallery.orig_left = jQuery('#' + card + ' .grav-gallery ul').css('margin-left').replace('px','');
    grav_gallery.last = jQuery('#' + card + ' .grav-gallery ul li:last');

    if ( grav_gallery.last.position().left &lt; 275 )
    jQuery('#' + card + ' a.grav-gallery-next').css({'background-position': '-39px 0'});
    else
    jQuery('#' + card + ' a.grav-gallery-next').css({'background-position': '-26px 0'});

    if ( 0 != grav_gallery.orig_left )
    jQuery('#' + card + ' a.grav-gallery-prev').css({'background-position': '0 0'});
    else
    jQuery('#' + card + ' a.grav-gallery-prev').css({'background-position': '-13px 0'});
    }
   }

   /*
    * A JavaScript implementation of the RSA Data Security, Inc. MD5 Message
    * Digest Algorithm, as defined in RFC 1321.
    * Version 2.1 Copyright (C) Paul Johnston 1999 - 2002.
    * Other contributors: Greg Holt, Andrew Kepert, Ydnar, Lostinet
    * Distributed under the BSD License
    * See http://pajhome.org.uk/crypt/md5 for more info.
    */

   var hexcase=0;var b64pad=\\;var chrsz=8;function hex_md5(s){return binl2hex(core_md5(str2binl(s),s.length*chrsz))}function b64_md5(s){return binl2b64(core_md5(str2binl(s),s.length*chrsz))}function str_md5(s){return binl2str(core_md5(str2binl(s),s.length*chrsz))}function hex_hmac_md5(a,b){return binl2hex(core_hmac_md5(a,b))}function b64_hmac_md5(a,b){return binl2b64(core_hmac_md5(a,b))}function str_hmac_md5(a,b){return binl2str(core_hmac_md5(a,b))}function md5_vm_test(){return hex_md5(\abc\)==\900150983cd24fb0d6963f7d28e17f72\}function core_md5(x,e){x[e&gt;&gt;5]|=0x80&lt;&lt;((e)%32);x[(((e+64)&gt;&gt;&gt;9)&lt;&lt;4)+14]=e;var a=1732584193;var b=-271733879;var c=-1732584194;var d=271733878;for(var i=0;i&lt;x.length;i+=16){var f=a;var g=b;var h=c;var j=d;a=md5_ff(a,b,c,d,x[i+0],7,-680876936);d=md5_ff(d,a,b,c,x[i+1],12,-389564586);c=md5_ff(c,d,a,b,x[i+2],17,606105819);b=md5_ff(b,c,d,a,x[i+3],22,-1044525330);a=md5_ff(a,b,c,d,x[i+4],7,-176418897);d=md5_ff(d,a,b,c,x[i+5],12,1200080426);c=md5_ff(c,d,a,b,x[i+6],17,-1473231341);b=md5_ff(b,c,d,a,x[i+7],22,-45705983);a=md5_ff(a,b,c,d,x[i+8],7,1770035416);d=md5_ff(d,a,b,c,x[i+9],12,-1958414417);c=md5_ff(c,d,a,b,x[i+10],17,-42063);b=md5_ff(b,c,d,a,x[i+11],22,-1990404162);a=md5_ff(a,b,c,d,x[i+12],7,1804603682);d=md5_ff(d,a,b,c,x[i+13],12,-40341101);c=md5_ff(c,d,a,b,x[i+14],17,-1502002290);b=md5_ff(b,c,d,a,x[i+15],22,1236535329);a=md5_gg(a,b,c,d,x[i+1],5,-165796510);d=md5_gg(d,a,b,c,x[i+6],9,-1069501632);c=md5_gg(c,d,a,b,x[i+11],14,643717713);b=md5_gg(b,c,d,a,x[i+0],20,-373897302);a=md5_gg(a,b,c,d,x[i+5],5,-701558691);d=md5_gg(d,a,b,c,x[i+10],9,38016083);c=md5_gg(c,d,a,b,x[i+15],14,-660478335);b=md5_gg(b,c,d,a,x[i+4],20,-405537848);a=md5_gg(a,b,c,d,x[i+9],5,568446438);d=md5_gg(d,a,b,c,x[i+14],9,-1019803690);c=md5_gg(c,d,a,b,x[i+3],14,-187363961);b=md5_gg(b,c,d,a,x[i+8],20,1163531501);a=md5_gg(a,b,c,d,x[i+13],5,-1444681467);d=md5_gg(d,a,b,c,x[i+2],9,-51403784);c=md5_gg(c,d,a,b,x[i+7],14,1735328473);b=md5_gg(b,c,d,a,x[i+12],20,-1926607734);a=md5_hh(a,b,c,d,x[i+5],4,-378558);d=md5_hh(d,a,b,c,x[i+8],11,-2022574463);c=md5_hh(c,d,a,b,x[i+11],16,1839030562);b=md5_hh(b,c,d,a,x[i+14],23,-35309556);a=md5_hh(a,b,c,d,x[i+1],4,-1530992060);d=md5_hh(d,a,b,c,x[i+4],11,1272893353);c=md5_hh(c,d,a,b,x[i+7],16,-155497632);b=md5_hh(b,c,d,a,x[i+10],23,-1094730640);a=md5_hh(a,b,c,d,x[i+13],4,681279174);d=md5_hh(d,a,b,c,x[i+0],11,-358537222);c=md5_hh(c,d,a,b,x[i+3],16,-722521979);b=md5_hh(b,c,d,a,x[i+6],23,76029189);a=md5_hh(a,b,c,d,x[i+9],4,-640364487);d=md5_hh(d,a,b,c,x[i+12],11,-421815835);c=md5_hh(c,d,a,b,x[i+15],16,530742520);b=md5_hh(b,c,d,a,x[i+2],23,-995338651);a=md5_ii(a,b,c,d,x[i+0],6,-198630844);d=md5_ii(d,a,b,c,x[i+7],10,1126891415);c=md5_ii(c,d,a,b,x[i+14],15,-1416354905);b=md5_ii(b,c,d,a,x[i+5],21,-57434055);a=md5_ii(a,b,c,d,x[i+12],6,1700485571);d=md5_ii(d,a,b,c,x[i+3],10,-1894986606);c=md5_ii(c,d,a,b,x[i+10],15,-1051523);b=md5_ii(b,c,d,a,x[i+1],21,-2054922799);a=md5_ii(a,b,c,d,x[i+8],6,1873313359);d=md5_ii(d,a,b,c,x[i+15],10,-30611744);c=md5_ii(c,d,a,b,x[i+6],15,-1560198380);b=md5_ii(b,c,d,a,x[i+13],21,1309151649);a=md5_ii(a,b,c,d,x[i+4],6,-145523070);d=md5_ii(d,a,b,c,x[i+11],10,-1120210379);c=md5_ii(c,d,a,b,x[i+2],15,718787259);b=md5_ii(b,c,d,a,x[i+9],21,-343485551);a=safe_add(a,f);b=safe_add(b,g);c=safe_add(c,h);d=safe_add(d,j)}return Array(a,b,c,d)}function md5_cmn(q,a,b,x,s,t){return safe_add(bit_rol(safe_add(safe_add(a,q),safe_add(x,t)),s),b)}function md5_ff(a,b,c,d,x,s,t){return md5_cmn((b&amp;c)|((~b)&amp;d),a,b,x,s,t)}function md5_gg(a,b,c,d,x,s,t){return md5_cmn((b&amp;d)|(c&amp;(~d)),a,b,x,s,t)}function md5_hh(a,b,c,d,x,s,t){return md5_cmn(b^c^d,a,b,x,s,t)}function md5_ii(a,b,c,d,x,s,t){return md5_cmn(c^(b|(~d)),a,b,x,s,t)}function core_hmac_md5(a,b){var c=str2binl(a);if(c.length&gt;16)c=core_md5(c,a.length*chrsz);var d=Array(16),opad=Array(16);for(var i=0;i&lt;16;i++){d[i]=c[i]^0x36363636;opad[i]=c[i]^0x5C5C5C5C}var e=core_md5(d.concat(str2binl(b)),512+b.length*chrsz);return core_md5(opad.concat(e),512+128)}function safe_add(x,y){var a=(x&amp;0xFFFF)+(y&amp;0xFFFF);var b=(x&gt;&gt;16)+(y&gt;&gt;16)+(a&gt;&gt;16);return(b&lt;&lt;16)|(a&amp;0xFFFF)}function bit_rol(a,b){return(a&lt;&lt;b)|(a&gt;&gt;&gt;(32-b))}function str2binl(a){var b=Array();var c=(1&lt;&lt;chrsz)-1;for(var i=0;i&lt;a.length*chrsz;i+=chrsz)b[i&gt;&gt;5]|=(a.charCodeAt(i/chrsz)&amp;c)&lt;&lt;(i%32);return b}function binl2str(a){var b=\\;var c=(1&lt;&lt;chrsz)-1;for(var i=0;i&lt;a.length*32;i+=chrsz)b+=String.fromCharCode((a[i&gt;&gt;5]&gt;&gt;&gt;(i%32))&amp;c);return b}function binl2hex(a){var b=hexcase?\0123456789ABCDEF\:\0123456789abcdef\;var c=\\;for(var i=0;i&lt;a.length*4;i++){c+=b.charAt((a[i&gt;&gt;2]&gt;&gt;((i%4)*8+4))&amp;0xF)+b.charAt((a[i&gt;&gt;2]&gt;&gt;((i%4)*8))&amp;0xF)}return c}function binl2b64(a){var b=\ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/\;var c=\\;for(var i=0;i&lt;a.length*4;i+=3){var d=(((a[i&gt;&gt;2]&gt;&gt;8*(i%4))&amp;0xFF)&lt;&lt;16)|(((a[i+1&gt;&gt;2]&gt;&gt;8*((i+1)%4))&amp;0xFF)&lt;&lt;8)|((a[i+2&gt;&gt;2]&gt;&gt;8*((i+2)%4))&amp;0xFF);for(var j=0;j&lt;4;j++){if(i*8+j*6&gt;a.length*32)c+=b64pad;else c+=b.charAt((d&gt;&gt;6*(3-j))&amp;0x3F)}}return c};

| Minimiert man das ganze noch mit einem JSMinifier wie
  `diesem <http://fmarcia.info/jsmin/test.html>`__, schrumpft das ganz
  noch einmal deutlich ein.
| Die so erhaltene Datei (Hier zum Download:
  `Hovercard.js.gz <{attach}/downloads/Hovercard.js.gz>`__
  )
| Läd man z.B. in MEINBLOG/wp-includes/js und trägt folgendes in die
  *funtions.php* des Themes ein:

::

    //Gravatar
    wp_enqueue_script( 'gprofiles', '/wp-includes/js/Hovercard.js', array( 'jquery' ), 'e', TRUE );
    ?>

.. |image0| image:: {static}/images/hovercard.jpg
   :alt: Screenshot einer Wordpress-Hovercard
   :class: alignleft size-full
   :width: 521px
   :height: 240px
   :target: {static}/images/hovercard.jpg

