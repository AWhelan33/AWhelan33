describe("Test clothing shop for example post", () => {
  it("loads the automation practice site", () => {
    cy.visit("http://automationpractice.com/index.php");
  });
  it("Check the homepage is loaded", () => {
    cy.get("[id=home-page-tabs]").should("be.visible");
  });

  it("Click on the tab labelled womens", () => {
    cy.contains("Women").click();
  });

  it("Check this loads the womens page", () => {
    cy.contains("You will find here all woman fashion collections.").should(
      "be.visible"
    );
  });

  it("Click on the search box", () => {
    cy.get("[id=search_query_top]").click();
  });

  it("type in dresses", () => {
    cy.get("[id=search_query_top]").type("dress");
  });
  it("click the search button", () => {
    cy.get("#searchbox > .btn").click();
  });

  it("check a result is returned", () => {
    cy.get('.heading-counter').should("be.visible");
  });
});
