import React, { useContext } from "react";
import NoImages from "./NoImages";
import Image from "./Image";
import { PhotoContext } from "../context/PhotoContext";

const Gallery = (props) => {
  const context = useContext(PhotoContext);
  const imageLink = context.images;
  let images;
  let noImages;
  // map variables to each item in fetched image array and return image component
  if (imageLink.length > 0) {
    images = imageLink.map((image) => {
      let id = image.id;
      let url = image.image_link;
      return <Image key={id} url={url} />;
    });
  } else {
    noImages = <NoImages />; // return 'not found' component if no images fetched
  }
  return (
    <div>
      <ul>{images}</ul>
      {noImages}
    </div>
  );
};

export default Gallery;
